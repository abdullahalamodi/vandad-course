// Updated fetch function with query parameters
import 'dart:convert';
import 'dart:io';

Future<dynamic> fetchProductData({Map<String, String>? queryParams}) async {
  try {
    HttpClient client = HttpClient();
    Uri uri = Uri.parse('http://localhost:8000/api/v1/products/1/').replace(
      queryParameters: queryParams,
    );

    HttpClientRequest request = await client.getUrl(uri);
    HttpClientResponse response = await request.close();

    String responseBody = await response.transform(utf8.decoder).join();

    if (response.statusCode == 200) {
      Map<String, dynamic> jsonData = jsonDecode(responseBody);
      print(jsonData);
      return jsonData;
    } else {
      // Try to parse error message from response if it's JSON
      try {
        Map<String, dynamic> errorData = jsonDecode(responseBody);
        print(
            'Error ${response.statusCode}: ${errorData['message'] ?? errorData['error'] ?? responseBody}');
        return {
          'statusCode': response.statusCode,
          'error': errorData['message'] ?? errorData['error'] ?? responseBody
        };
      } catch (e) {
        // If response isn't JSON, just use the raw body
        print('Error ${response.statusCode}: $responseBody');
        return {'statusCode': response.statusCode, 'error': responseBody};
      }
    }
  } catch (e) {
    print('Error fetching data: $e');
    return null;
  }
}

// Updated server handler
Future<void> startServer() async {
  try {
    final server = await HttpServer.bind(InternetAddress.anyIPv4, 8080);
    print('Server running on http://localhost:8080');

    await for (HttpRequest request in server) {
      try {
        if (request.method == 'GET' && request.uri.path == '/product') {
          // Pass query parameters from incoming request
          var result = await fetchProductData(queryParams: request.uri.queryParameters);

          request.response.headers.contentType = ContentType.json;

          if (result != null) {
            request.response.write(
              jsonEncode({'data': result.data, 'status': 'success'}),
            );
          } else {
            request.response.statusCode = 500;
            request.response.write(
              jsonEncode(
                {'status': 'error', 'message': 'Failed to fetch search data'},
              ),
            );
          }
        } else {
          request.response.statusCode = 404;
          request.response.write(jsonEncode({'status': 'error', 'message': 'Endpoint not found'}));
        }
      } catch (e) {
        request.response.statusCode = 500;
        request.response.write(jsonEncode({'status': 'error', 'message': 'Server error: $e'}));
      } finally {
        await request.response.close();
      }
    }
  } catch (e) {
    print('Server error: $e');
  }
}

void main() async {
  await startServer();
}
