extends Area2D

@onready var game_manager = $"../GameManager"

func _on_body_entered(body):
	if body.name == "player":
		game_manager.level_complete()
