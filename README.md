# STEM Carnival

<i>Made for the Landstown High School STEM Carnival. The server records the values from sensors which are sent through POST requests. The client sends sensor data to the server. The server stores the sensor data for each player in Excel Workbooks for easy data manipulation.</i>

## Server

The server accepts POST requests to /game/&lt;the UUID of the game&gt;. This devide would contain an NFC reader where players would scan their cards. The reader would send the player's UUID to the server and the server would mark the game as being played by the player. The player has to scan at the end to end the game.

There are measures in place to ensure that a player can not be playing a game at the same time. This may occur if they share their card with their friend. Also, a player can not scan their card while the game is being played by another player.

## Client

The client records values from connected sensors when the player is playing. The values are send to the server along with the game UUID and the sensor UUID. These UUIDs are hard coded into a secrets file located on the client.

There are measures to ensure that sensor data is not accepted by the server if a player is not playing.

## Compatability
 - Raspberry Pico W