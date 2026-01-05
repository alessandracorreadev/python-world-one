from time import sleep
import emoji

print('-'*33)
print("Countdown to the fireworks show!")
print('-'*33)

for countdown in range(10, 0, -1):
    print(countdown)
    sleep(1)
print(emoji.emojize(f"BOOM BOOM BOOM! :fireworks: :sparkler:"))