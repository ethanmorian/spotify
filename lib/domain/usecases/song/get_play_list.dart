import 'package:dartz/dartz.dart';
import 'package:spotify/core/usecase/usecase.dart';

import '../../../service_locator.dart';
import '../../repositories/song/song.dart';

class GetPlayListUseCase implements UseCase<Either, dynamic> {
  @override
  Future<Either> call({params}) async {
    return sl<SongRepository>().getPlayList();
  }
}
