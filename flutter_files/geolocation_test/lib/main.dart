import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'API.dart';
import 'dart:convert';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Audio Reality',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Audio Reality'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String? url;
  var data;
  String queryText = "Description";

  Position? _position;

  void _getCurrentLocation() async {
    Position position = await _determinePosition();
    setState(() {
      _position = position;
    });
  }

  Future<Position> _determinePosition() async {
    LocationPermission permission;
    permission = await Geolocator.checkPermission();
    if (permission == LocationPermission.denied) {
      permission = await Geolocator.requestPermission();
      if (permission == LocationPermission.denied) {
        return Future.error('Location Permissions are denied');
      }
    }
    return await Geolocator.getCurrentPosition();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Audio Reality"),
      ),
      body: Center(child: Text(queryText)),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () async {
          _getCurrentLocation();
          url =
              'http://127.0.0.1:5000/api?Query=${_position?.latitude ?? ''}/${_position?.longitude ?? ''}';
          var parsedUrl = Uri.parse(url.toString());
          debugPrint('$parsedUrl');
          data = await getData(parsedUrl).timeout(const Duration(minutes: 5));
          var decodedData = jsonDecode(data);
          setState(() {
            queryText = decodedData.toString();
          });
        },
        tooltip: "Get location data",
        icon: const Icon(Icons.location_searching),
        label: const Text("Get location data"),
      ),
    );
  }
}
