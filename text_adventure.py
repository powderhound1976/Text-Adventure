with open('game_instructions.txt') as intro:
    intro = intro.read()

with open('map.txt') as map:
    map = map.read()

print(intro)

player = {
    'inventory': ['strength'],
    'location': 'foyer'
}

monster = {
    'health': ['100'],
    'sanity': ['100'],
}

monster_alive = True


actions = [
    'enter foyer', 'enter parlor', 'enter library', 'enter kitchen',
    'enter pantry', 'inventory', 'take all items', 'take [item]', 'items',
    'conversation', 'map', 'quit', 'hypnotize', 'karate chop']

rooms = {
    'foyer': {
        'description': 'This is the foyer.',
        'items': ['jam', 'bread'],
        'exits': ['parlor', 'library']},
    'parlor': {
        'description': 'This is the Parlor.',
        'items': [''],
        'exits': ['foyer', 'kitchen']},
    'library': {
        'description': 'This is the Library.',
        'items': ['book', 'letter opener'],
        'exits': ['foyer', 'kitchen']},
    'kitchen': {
        'description': 'This is the Kitchen.',
        'items': ['knife', 'pot'],
        'exits': ['parlor', 'library', 'pantry']},
    'pantry': {
        'description': 'This is the Pantry.',
        'items': ['sugar'],
        'exits': ['kitchen']}}


while True:
    location = player['location']
    action = input(
        "Enter a command like 'enter [room name]', 'inventory',"
        " 'take all items','\ntake [item]', 'items', 'conversation',"
        " 'map', 'quit'\nWhat would you like to do? :").split()

    if action[0] == 'map':
        print(map)
    elif action[0] == 'conversation':
        with open('conversation.txt') as c:
            c = c.read()
            print(c)
    elif action[0] == 'inventory':
        print('\nRight now you have', player['inventory'], '\n')
    elif action[0] == 'quit':
        print('OK! Thanks for playing!')
        break
    elif action[0] == 'items':
        print('\nThis room contains', rooms[player['location']]["items"], '\n')
    elif action[0] == 'enter':
        if action[1] in rooms[player['location']]['exits']:
            player['location'] = action[1]
            print('\nOK, you just moved to the', player['location'], '.\n')
            if player['location'] == 'pantry':
                while monster_alive is True:
                    if '100' in monster['health'] and '100' in monster[
                            'sanity']:
                        monster_action = input(
                            "Watch out! A monster is attacking you!\n\nTo slay"
                            " him you must hit and also hypnotize him.\n"
                            "(Use the commands 'karate chop' or 'hypnotize'):"
                            "\nWhat would you like to do? "
                        ).split()
                    elif (
                        '100' in monster['health'] and '100' not in monster[
                            'sanity']) or ('100' not in monster[
                                'health'] and '100' in monster['sanity']):
                        monster_action = input(
                            '\nYou are hurting the monster but you have not'
                            ' slayed him.\n\n'
                            'To slay him you must hit and also hypnotize'
                            ' him.\n'
                            "(Use the commands 'karate chop' or 'hypnotize'):"
                            "\nWhat would you like to do? "
                        ).split()
                    if monster_action[0] == 'karate':
                        monster['health'] = '0'
                        print(
                            "\nGood job, you have injured the monster.\n",
                            "His health is now", monster['health'], '.')
                    if monster_action[0] == 'hypnotize':
                        monster['sanity'] = '0'
                        print(
                            '\nGood job, you have driven the monster crazy.'
                            '\nHis sanity is now', monster['sanity'], '\n')
                    if '0' in monster['health'] and '0' in monster['sanity']:
                        print(
                            '\nThere is a monster in this room'
                            ' but you slayed it.\n')
                        monster_alive = False
            elif player['location'] == 'library':
                talk = input(
                    'Hello, Im a ghost in the library. '
                    'I am lonely.  I like conversation.  If you really do'
                    " not want to converse type 'stop'"
                    '\n\n Will you talk to me? : ')
                with open('conversation.txt', 'w') as converse:
                    converse.write(
                        '\nGhost: Hello, Im a ghost in the library. '
                        'I am lonely.  I like conversation.  If you really do'
                        " not want to converse type 'stop'"
                        '\nWill you talk to me? : ')
                    converse.write(talk)
                    converse.write('\n')
                    if talk == 'stop':
                        break
                while True:
                    more_talk = input(
                        "\nThat's interesting talk to me some more? :\n")
                    with open('conversation.txt', 'a') as more_converse:
                        more_converse.write(
                            "\nGhost: That's interesting"
                            " talk to me some more?: ")
                        more_converse.write('\nAdventurer: ')
                        more_converse.write(more_talk)
                        more_converse.write('\n')
                    if more_talk == 'stop':
                        break
        else:
            print('\nYou cannot move to the', action[1], 'from the', player[
                'location'], '. Try again.\n')
    elif action[0] == 'take':
        current_take = []
        if action[1] in rooms[player['location']][
                'items'] and action[1] not in player['inventory']:
            # Add item picked up to player inventory
            player['inventory'].append(action[1])
            current_take.append(action[1])
            print('\nOK, you have added', current_take, 'to your inventory.\n')
            # Remove item from items in room
            rooms[player['location']]['items'].remove(action[1])
        elif action[2]:
            i = len(rooms[player['location']]['items'])
            while i > 0:
                for item in rooms[player['location']]['items']:
                    player['inventory'].append(item)
                    current_take.append(item)
                    rooms[player['location']]['items'].remove(item)
                i = i - 1
            print('\nOK, you have added', current_take, 'to your inventory.')
