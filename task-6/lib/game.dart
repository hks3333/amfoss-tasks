import 'dart:ui';
import 'package:flame/game.dart';
import 'player.dart';
import 'world.dart';
import 'directions.dart';

class BunnyGame extends FlameGame {
  final BunnyPlayer _bunnyPlayer = BunnyPlayer();
  final BunnyWorld _bunnyWorld = BunnyWorld();

  onArrowKeyChanged(Direction direction) {
    _bunnyPlayer.direction = direction;
  }

  @override
  Future<void> onLoad() async {
    super.onLoad();
    await add(_bunnyWorld);
    await add(_bunnyPlayer);
    _bunnyPlayer.position = _bunnyWorld.size / 1.5;
    camera.followComponent(_bunnyPlayer,
        worldBounds:
            Rect.fromLTRB(0, 0, _bunnyWorld.size.x, _bunnyWorld.size.y));
  }
}
