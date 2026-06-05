extends Node

var score = 0
var elapsed_time: float = 0.0
var timer_running: bool = false
var player_name: String = "Anonymous"

@onready var door = $"../Door"
@onready var timer_label = $"../UI/TimerLabel"
@onready var coin_label = $"../UI/CoinLabel"
@onready var name_panel = $"../UI/NamePanel"
@onready var name_input = $"../UI/NamePanel/NameInput"
@onready var start_button = $"../UI/NamePanel/StartButton"
@onready var main_menu = $"../UI/MainMenu"
@onready var play_button = $"../UI/MainMenu/PlayButton"

func _ready():
	get_tree().paused = true
	timer_running = false
	print(play_button)
	timer_label.text = "0.00"
	coin_label.text = "Coins: 0/6"
	main_menu.visible = true
	name_panel.visible = false
	play_button.pressed.connect(_on_play_pressed)
	start_button.pressed.connect(_on_start_pressed)

func _on_play_pressed():
	print("play pressed")
	main_menu.visible = false
	name_panel.visible = true

func _on_start_pressed():
	player_name = name_input.text
	if player_name == "":
		player_name = "Anonymous"
	name_panel.visible = false
	get_tree().paused = false
	timer_running = true

func _process(delta):
	if timer_running:
		elapsed_time += delta
		timer_label.text = "%.2f" % elapsed_time

func add_point():
	score += 1
	coin_label.text = "Coins: %d/6" % score
	if score == 6:
		door.unlock()

func level_complete():
	timer_running = false
	timer_label.text = "Finished! %.2f" % elapsed_time
	submit_time(player_name, elapsed_time)

func submit_time(p_name: String, time: float):
	var http = HTTPRequest.new()
	add_child(http)
	http.request_completed.connect(_on_request_completed)
	var body = JSON.stringify({"name": p_name, "time": time})
	var headers = ["Content-Type: application/json"]
	http.set_tls_options(TLSOptions.client_unsafe())
	http.request("https://10.248.126.228:8600/submit", headers, HTTPClient.METHOD_POST, body)

func _on_request_completed(result, response_code, headers, body):
	print("Result: ", result)
	print("Response code: ", response_code)
