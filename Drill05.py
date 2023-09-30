from pico2d import *
import random
import math

TUK_WIDTH, TUK_HEIGHT = 1280, 720
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


def handle_events():
    global running
    global x, y
    global m_x,m_y
    global h_x, h_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            m_x, m_y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
h_x, h_y = random.randrange(0, TUK_WIDTH), random.randrange(0, TUK_HEIGHT)  # 초기 위치 설정
hide_cursor()

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    dx, dy = h_x - x, h_y - y
    distance = math.sqrt(dx ** 2 + dy ** 2)
    if distance > 0:
        x += dx / distance * 10
        y += dy / distance * 10
    if dx >= 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif dx<0:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)
    # 손과 캐릭터 사이의 거리가 일정 값 이하면 새로운 랜덤 위치에 hand 그리기
    if distance <= 30:
        h_x, h_y = random.randrange(0, TUK_WIDTH), random.randrange(0, TUK_HEIGHT)

    hand.draw(h_x, h_y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()