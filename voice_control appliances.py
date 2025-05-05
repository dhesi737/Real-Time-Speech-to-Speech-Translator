import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        print("Could not connect to the speech service.")
        return ""

def main():
    print("Voice-controlled light system started. Say a command.")
    while True:
        command = listen_command()

        if "turn on the light" in command:
            print("✅ Light turned ON")
        elif "turn off the light" in command:
            print("❌ Light turned OFF")
        elif "exit" in command or "stop" in command:
            print("👋 Exiting program.")
            break

if __name__ == "__main__":
    main()
