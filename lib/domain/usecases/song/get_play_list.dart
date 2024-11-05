import 'package:dartz/dartz.dart';
import 'package:spotify/core/usecase/usecase.dart';
import 'package:spotify/data/repositories/song/song_repository_impl.dart';

import '../../../service_locator.dart';

class GetPlayListUseCase implements UseCase<Either, dynamic> {
  @override
  Future<Either> call({params}) async {
    return sl<SongRepositoryImpl>().getPlayList();
  }
}