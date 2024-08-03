import 'package:daangn_home/repository/contents_repository.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';
import 'package:intl/intl.dart';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  late String currentLocation;
  ContentsRepository contentsRepository = ContentsRepository();
  final Map<String, String> locationTypeToString = {
    "ara": "아라동",
    "ora": "오라동",
    "donam": "도남동",
  };

  @override
  void initState() {
    super.initState();
    currentLocation = "ara";
  }

  final oCcy = NumberFormat("#,###", "ko_KR");

  String calcStringToWon(String priceString) {
    if (priceString=="무료나눔") return priceString;
    return "${oCcy.format(int.parse(priceString))}원";
  }

  PreferredSizeWidget _appbarWidget() {
    return AppBar(
      title: GestureDetector(
        onTap: () {
          print("click");
        },
        child: PopupMenuButton<String>(
          offset: const Offset(0, 25),
          shape: ShapeBorder.lerp(
            RoundedRectangleBorder(borderRadius: BorderRadius.circular(10.0)),
            RoundedRectangleBorder(borderRadius: BorderRadius.circular(10.0)),
            1,
          ),
          onSelected: (String where) {
            setState(() {
              currentLocation = where;
            });
          },
          itemBuilder: (BuildContext context) {
            return [
              const PopupMenuItem(
                value: "ara",
                child: Text("아라동"),
              ),
              const PopupMenuItem(
                value: "ora",
                child: Text("오라동"),
              ),
              const PopupMenuItem(
                value: "donam",
                child: Text("도남동"),
              ),
            ];
          },
          child: Row(
            children: [
              Text(locationTypeToString[currentLocation]!),
              const Icon(Icons.arrow_drop_down),
            ],
          ),
        ),
      ),
      elevation: 1,
      actions: [
        IconButton(
          onPressed: () {},
          icon: const Icon(Icons.search),
        ),
        IconButton(
          onPressed: () {},
          icon: const Icon(Icons.tune),
        ),
        IconButton(
          onPressed: () {},
          icon: SvgPicture.asset(
            "assets/svg/bell.svg",
            width: 22,
          ),
        ),
      ],
    );
  }

  _loadContents() {
    return contentsRepository.loadContentsFromLocation(currentLocation);
  }

  _makeDataList(List<Map<String, dynamic>> data) {
    return ListView.separated(
      padding: const EdgeInsets.symmetric(horizontal: 10),
      itemBuilder: (BuildContext context, int index) {
        return Container(
            padding: const EdgeInsets.symmetric(vertical: 10),
            child: Row(
              children: [
                ClipRRect(
                    borderRadius: const BorderRadius.all(Radius.circular(10)),
                    child: Image.asset(
                      data[index]["image"]!,
                      width: 100,
                      height: 100,
                    )),
                Expanded(
                  child: Container(
                    height: 100,
                    padding: const EdgeInsets.only(left: 20),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          data[index]["title"]!,
                          overflow: TextOverflow.ellipsis,
                          style: const TextStyle(fontSize: 15),
                        ),
                        const SizedBox(
                          height: 5,
                        ),
                        Text(
                          data[index]["location"]!,
                          style: TextStyle(
                              fontSize: 12,
                              color: Colors.black.withOpacity(0.3)),
                        ),
                        const SizedBox(
                          height: 5,
                        ),
                        Text(
                          calcStringToWon(data[index]["price"]!),
                          style: const TextStyle(fontWeight: FontWeight.w500),
                        ),
                        Expanded(
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.end,
                            crossAxisAlignment: CrossAxisAlignment.end,
                            children: [
                              SvgPicture.asset(
                                "assets/svg/heart_off.svg",
                                width: 13,
                                height: 13,
                              ),
                              const SizedBox(
                                width: 5,
                              ),
                              Text(data[index]["likes"]!),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ],
            ));
      },
      itemCount: 10,
      separatorBuilder: (BuildContext context, int index) {
        return Container(
          height: 1,
          color: Colors.black.withOpacity(0.4),
        );
      },
    );
  }

  Widget _bodyWidget() {
    return FutureBuilder(
      future: _loadContents(),
      builder: (BuildContext context, dynamic snapshot) {
        if (snapshot.connectionState != ConnectionState.done) {
          return const Center(
            child: CircularProgressIndicator(),
          );
        }

        if (snapshot.hasError) {
          return const Center(
            child: Text("데이터 오류"),
          );
        }

        if (snapshot.hasData) {
          return _makeDataList(snapshot.data);
        }

        return const Center(
          child: Text("해당 지역에 데이터가 없습니다."),
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: _appbarWidget(),
      body: _bodyWidget(),
    );
  }
}
