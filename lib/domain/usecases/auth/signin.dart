import 'package:dartz/dartz.dart';
import 'package:spotify/core/usecase/usecase.dart';
import 'package:spotify/domain/repositories/auth/auth.dart';

import '../../../data/models/auth/signin_user_req.dart';
import '../../../service_locator.dart';

class SigninUseCase implements UseCase<Either, SigninUserReq> {
  @override
  Future<Either> call({SigninUserReq? params}) async {
    return await sl<AuthRepository>().signin(params!);
  }
}
