import 'package:flame/components.dart';
import 'directions.dart';

class BunnyPlayer extends SpriteComponent with HasGameRef {
  BunnyPlayer() : super(size: Vector2.all(100.0));

  @override
  Future<void> onLoad() async {
    super.onLoad();
    sprite = await gameRef.loadSprite('bunny.png');
    position = gameRef.size / 2;
  }

  Direction direction = Direction.none;

  @override
  void update(double dt) {
    super.update(dt);
    updatePosition(dt);
  }

  updatePosition(double dt) {
    switch (direction) {
      case Direction.up:
        position.y -= 2;
        break;
      case Direction.down:
        position.y += 2;
        break;
      case Direction.left:
        position.x -= 2;
        break;
      case Direction.right:
        position.x += 2;
        break;
      case Direction.none:
        break;
    }
  }
}
