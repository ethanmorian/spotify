import 'package:spotify/data/sources/auth/auth_firebase_service.dart';
import 'package:spotify/domain/repositories/auth/auth.dart';

import '../../../service_locator.dart';
import '../../models/auth/create_user_req.dart';

class AuthRepositoryImpl extends AuthRepository {
  @override
  Future<void> signin() {
    // TODO: implement signin
    throw UnimplementedError();
  }

  @override
  Future<void> signup(CreateUserReq createUserReq) async {
    await sl<AuthFirebaseService>().signup(createUserReq);
  }
}
