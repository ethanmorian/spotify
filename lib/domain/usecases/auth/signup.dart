import 'package:dartz/dartz.dart';
import 'package:spotify/core/usecase/usecase.dart';
import 'package:spotify/domain/repositories/auth/auth.dart';

import '../../../data/models/auth/create_user_req.dart';
import '../../../service_locator.dart';

class SignupUseCase implements UseCase<Either, CreateUserReq> {
  @override
  Future<Either> call({CreateUserReq? params}) async {
    return await sl<AuthRepository>().signup(params!);
  }
}
