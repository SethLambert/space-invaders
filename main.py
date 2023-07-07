from turtle import Screen
from hero_laser import HeroLaser
from enemy_ship import EnemyShip
from enemy_bomb import EnemyBomb
from hero_ship import HeroShip
from home_base import HomeBase
import time
from level_setup import levels
from text_display import TextDisplay

screen = Screen()
screen.bgcolor("black")
screen.setup(width=400, height=600)
screen.title("Invaders From Uranus")
screen.tracer(0)

hero_ship = HeroShip((0,-260))
text_display = TextDisplay()
hero_lasers = [HeroLaser() for i in range(40)]
enemy_bombs = [EnemyBomb() for i in range(20)]

def fire_laser():
    for laser in hero_lasers:
        if laser.moving != True:
            laser.fire()
            break

screen.listen()
screen.onkey(hero_ship.go_left, "Left")
screen.onkey(hero_ship.go_right, "Right")
screen.onkey(fire_laser, "space")

game_is_on = True

level = 1
enemy_ships = []
for i in range(len(levels[f'{level}']['positions'])):
    enemy_ship = EnemyShip(levels[f'{level}']['positions'][i], levels[f'{level}']['colors'][i])
    enemy_ships.append(enemy_ship)
    
home_bases = []
for i in range(len(levels[f'{level}']['base_positions'])):
    home_base = HomeBase(levels[f'{level}']['base_positions'][i])
    home_bases.append(home_base)

counter = 0
bomb_to_fire = 0
advance = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for laser in hero_lasers:
        laser.move(hero_ship.xcor())
        for ship in enemy_ships:
            #detect collision with laser and enemy ship
            if laser.distance(ship) < 25:
                ship.destroy()
                enemy_ships.remove(ship)
                laser.hit(hero_ship.xcor())
                if len(enemy_ships) == 0:
                    text_display.update_text(f"Game Complete!\n{len(home_bases)} home bases were saved.", 'green')    
                    screen.update()
                    game_is_on = False
                    break
        for bomb in enemy_bombs: 
            if laser.distance(bomb) < 25:
                bomb.hit()
        
    for ship in enemy_ships:
        if advance:
            ship.move()
        if ship.distance(hero_ship) < 25:
            hero_ship.hit()
            text_display.update_text("Game Over", 'red')
            screen.update()
            game_is_on = False
            break
        for base in home_bases:
            if ship.distance(base) < 25:
                base.hit()
                home_bases.remove(base)
                text_display.update_text("Game Over", 'red')
                screen.update()
                game_is_on = False
                break
        
            
    if counter % 30 == 0:
        if bomb_to_fire < 20:
            enemy_bombs[bomb_to_fire].fire()
            bomb_to_fire += 1
        else:
            bomb_to_fire = 0   
                     
    for bomb in enemy_bombs:
        bomb.move()
        if bomb.distance(hero_ship) < 25:
            bomb.hideturtle()
            hero_ship.hit()
            text_display.update_text("Game Over", 'red')
            screen.update()
            game_is_on = False
            break
        for base in home_bases:
            if bomb.distance(base) < 25:
                bomb.hit()
                base.hit()
                home_bases.remove(base)

    if advance:
        advance = False
    else:
        advance = True
        
    counter += 1


screen.exitonclick()
