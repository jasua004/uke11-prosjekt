extends AnimatableBody2D
var player_on_platform

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	#print(player_on_platform)
	#print($AnimationPlayer.speed_scale)
	if player_on_platform:
		$AnimationPlayer.speed_scale=15	
	else:
		$AnimationPlayer.speed_scale=1	

func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.is_in_group("player"):
		player_on_platform = true

func _on_area_2d_body_exited(body: Node2D) -> void:
	if body.is_in_group("player"):
		player_on_platform = false
