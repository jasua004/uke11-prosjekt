extends Node

var score = 0
var elapsed_time: float = 0.0
var timer_running: bool = false

@onready var door = $"../Door"
@onready var timer_label = $"../UI/TimerLabel"

func _ready():
	timer_running = true

func _process(delta):
	if timer_running:
		elapsed_time += delta
		timer_label.text = "%.2f" % elapsed_time

func add_point():
	score += 1
	print(score)
	if score == 6:
		door.unlock()

func level_complete():
	timer_running = false
	timer_label.text = "Finished %.2f" % elapsed_time
	print("Time: ", elapsed_time)
