from gtts import gTTS
from playsound import playsound
value='Gokulan p k is my master who created me ,he was the best python developer in the world still want more connect on github,best wishes !..'
language='en'
object =gTTS(text=value,lang=language,slow=False)
object.save("python.mp3")
playsound("python.mp3")