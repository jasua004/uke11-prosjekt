extends AnimatableBody2D

var speed = 200
var direction = 1

func _physics_process(delta):
	var motion = Vector2(speed * direction, 0)
	var collision = move_and_collide(motion * delta)

	if collision:
		direction *= -1

		var body = collision.get_collider()
		if body.is_in_group("player"):
				get_tree().reload_current_scene()
