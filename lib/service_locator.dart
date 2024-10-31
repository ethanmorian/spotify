import 'package:get_it/get_it.dart';
import 'package:spotify/data/repositories/auth/auth_repository_impl.dart';
import 'package:spotify/data/sources/auth/auth_firebase_service.dart';
import 'package:spotify/domain/repositories/auth/auth.dart';

final sl = GetIt.instance;

Future<void> initializeDependencies() async {
  sl.registerSingleton<AuthFirebaseService>(
    AuthFirebaseServiceImpl(),
  );
  sl.registerSingleton<AuthRepository>(
    AuthRepositoryImpl(),
  );
}