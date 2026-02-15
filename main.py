from vision import check_focus
from monitor import StudyMonitor
from model import predict_confusion
from analytics import save_session, show_stats


monitor = StudyMonitor()

while True:
    print("\nSmart Study Monitor")
    print("1. Start Study")
    print("2. End Study")
    print("3. Analyze Notes")
    print("4. Show Analytics")
    print("5. Exit")
    print("6. Check Focus (OpenCV)")


    choice = input("Choose option: ")

    if choice == "1":
        monitor.start()

    elif choice == "2":
        duration = monitor.end()
        if duration > 0:
            save_session(duration)

    elif choice == "3":
        notes = input("Paste notes: ")
        result = predict_confusion(notes)
        print("Confusion Prediction:", result)

    elif choice == "4":
        show_stats()

    elif choice == "5":
        break
        
    elif choice == "6":
        focused = check_focus()

        if focused:
           print("Face detected — You look focused.")
        else:
           print("No face detected — Possible distraction.")
 


