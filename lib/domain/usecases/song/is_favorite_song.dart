import 'package:spotify/core/usecase/usecase.dart';
import 'package:spotify/domain/repositories/song/song.dart';

import '../../../service_locator.dart';

class IsFavoriteSongUseCase implements UseCase<bool, String> {
  @override
  Future<bool> call({String? params}) async {
    return await sl<SongRepository>().isFavoriteSong(params!);
  }
}