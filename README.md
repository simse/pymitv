# pymitv
A Python based control of the Mi Tv 3

### Accessing the local API exposed by the TV
First of all you need to get your TVs IP address. 

##### Check TV status
To check if the TV is on, use the following request:
`http://TV_IP:6095/request?action=isalive`

The above will return something along the lines of:
```json
{
	"status": 0,
	"msg": "success",
	"data": {
		"devicename": "客厅的小米电视",
		"ip": "TV_IP:6095",
		"feature": ["power"],
		"url": ["http:\/\/bilibili.kankanews.com\/video\/av\\d+\/", "http:\/\/www.bilibili.tv\/video\/av\\d+\/"],
		"platform": 606,
		"build": 1381,
		"version": 16777500
	}
}
```

##### Send keystroke
To send a keystroke use the following request:
`http://TV_IP:6095/controller?action=keyevent&keycode=KEYCODE`

Instead of `KEYCODE`, you should write an actual keycode. These are the available ones:
Key/button | keycode | action
--- | --- | ---
On/off toggle | `power` | Turns the TV on or off
Up | `up` | Goes up
Down | `down` | Goes down
Left | `left` | Goes left
Right | `right` | Goes right
Enter | `enter` | Affirms selection
Home | `home` | Returns to home screen
Back | `back` | Goes one step back
Menu | `menu` | Opens options menu
Volume up | `volumeup` | Increases volume by 1
Volume down | `volumedown` | Decreases volume by 1
