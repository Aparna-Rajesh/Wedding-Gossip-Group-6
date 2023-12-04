import random
import heapq
import math 


class Player():
    def __init__(self, id, team_num, table_num, seat_num, unique_gossip, color, turns):
        self.round_number = 1
        self.move_counter = random.randint(0, 9)
        self.id = id
        self.team_num = team_num
        self.table_num = table_num
        self.seat_num = seat_num
        self.color = color
        self.prev_gossip = [unique_gossip]
        self.unique_gossip = unique_gossip
        self.gossip_list = [unique_gossip]
        self.good_gossips = [unique_gossip] # keep sorted desc
        self.group_score = 0
        self.individual_score = 0
        self.total_rounds = turns 
        #dictionary template -> dict3 = {'gossip_shared': '15,16,77', 'gossip_score': 55}
        #dictionary_temp = {'gossip_shared': [], 'gossip_score': unique_gossip}
        #list of dictionaries 
        self.shared_gossip = {}
        self.shared_gossip[unique_gossip] = []
        #heapq.heappush(self.gossip_pq, (dictionary_temp['gossip_score'], dictionary_temp))
        #initialize a pq for gossip initlaized with just your own gossip shared with nobody 




    # At the beginning of a turn, players should be told who is sitting where, so that they can use that info to decide if/where to move
    def observe_before_turn(self, player_positions):
        #can use our current data structure to see the optimal value to score 
        #who to share to 
        #and what value
        self.round_number +=1 
        self.move_counter +=1


    # At the end of a turn, players should be told what everybody at their current table (who was there at the start of the turn)
    # did (i.e., talked/listened in what direction, or moved)
    def observe_after_turn(self, player_actions):
        #figure out what is given in player_actions 

        #this function is currently null 

        #try:
        action = player_actions[0]
            #print("printing player action")
            #print(action)
        #except:
            #print("there are no player actions ")
        #if action != "":
            
        
        
        '''my_action = "talk"
        #get whatever our current action is 
        for action in player_actions:
            player_id = action[0]
            actual_action = action[1][0]
            success = action[1][1] # not super sure on this one 
            if player_id == self.id: 
                my_action = actual_action
                break 
        if my_action == 'talk':
            #see who we shared w 
            for action in player_actions:
                player_id = action[0]
                actual_action = action[1][0]
                success = action[1][1] # not super sure on this one - how do we know if they nodded? 
                #add another player to our gossip id 
                self.shared_gossip[unique_gossip].append(player_id)
                #update those spoken to 
        if my_action == 'listen':
            #save to pq 
            new_gossip = set(self.gossip_list-self.prev_gossip)
            self.prev_gossip = self.gossip_list
            for action in player_actions:
                player_id = action[0]
                actual_action = action[1][0]
                success = action[1][1] # not super sure on this one
                #d_temp = {'gossip_shared': [self.id], 'gossip_score': player_id}
                #heapq.heappush(self.gossip_pq, (d_temp['gossip_score'], d_temp))
                
                #need to figure out new gossip that we heard and from who? .
                new_gossip = set(self.gossip_list-self.prev_gossip)
                self.prev_gossip = self.gossip_list'''





        #if you talked, add whichever success listens to set for that specific gossip 

        #if you listen, add that new gossip to your pq 

    def get_action(self):
        #get heuristic of your current pq 
        #and status of players in radius around you 
        #use a ratio to dictate the optimal split of the # of listners, talkers, and movers
        

        # return 'talk', 'left', <gossip_number>
        # return 'talk', 'right', <gossip_number>
        # return 'listen', 'left', 
        # return 'listen', 'right', 
        # return 'move', priority_list: [[table number, seat number] ...]

        #action_type = random.randint(0, 2)

        #action_type = random.randint(0, 9)
        if self.move_counter >= 9: 
            self.move_counter = 0 
            table1 = random.randint(0, 9)
            seat1 = random.randint(0, 9)

            table2 = random.randint(0, 9)
            while table2 == table1:
                table2 = random.randint(0, 9)

            seat2 = random.randint(0, 9)
            #print('moving to' + str(table2))
            return 'move', [[table1, seat1], [table2, seat2]]
        #get gossip count score and round number 
        gossip_score = self.get_heuristic()
        action,val = self.decide_torl(gossip_score)
        #print(action)
        if action == 'talk':
            #grab one of the top 5 values to speak 
            #print('talking with a value of ' + str(val))
            #print("talker gossip len" + str(len(self.gossip_list)))
            if self.round_number%2 == 0: #is even, so do this 
                return 'talk','right',val

            else: 
                return 'talk','left',val
        if action == 'listen':
            #print('listening')
            #print("this is the length of this players gossip" + str(len(self.gossip_list)))
            if self.round_number%2 == 0:
                return 'listen', 'left'
            else: 
                return 'listen', 'right'
            
        else: #move 
            table1 = random.randint(0, 9)
            seat1 = random.randint(0, 9)

            table2 = random.randint(0, 9)
            while table2 == table1:
                table2 = random.randint(0, 9)

            seat2 = random.randint(0, 9)
            #print('moving to' + str(table2))
            return 'move', [[table1, seat1], [table2, seat2]]


        # talk
        if action_type <= 2:
            direction = random.randint(0, 1)
            gossip = random.choice(self.gossip_list)
            # left
            if direction == 0:
                return 'talk', 'left', gossip
            # right
            else:
                return 'talk', 'right', gossip
        
        # listen
        elif action_type > 2 and action_type <9:
            direction = random.randint(0, 1)
            # left
            if direction == 0:
                return 'listen', 'left'
            # right
            else:
                return 'listen', 'right'

        # move
        else:
            table1 = random.randint(0, 9)
            seat1 = random.randint(0, 9)

            table2 = random.randint(0, 9)
            while table2 == table1:
                table2 = random.randint(0, 9)

            seat2 = random.randint(0, 9)

            return 'move', [[table1, seat1], [table2, seat2]]
    
    def feedback(self, feedback):
        listener_cnt = len(feedback)
        # based on the feedback, retire the gossips that two other persons have already known
        # remove from self.good_gossips

    def get_gossip(self, gossip_item, gossip_talker):
        #if you recieve an item of gossip, you can add to your list 
        self.good_gossips.append(gossip_item) # gossip_list added by simulator in wedding_gossip.py
        self.good_gossips.sort(reverse=True)

    def get_heuristic(self):
        #aquire top gosip 
        gossips = self.good_gossips
        #get top 5 vals if exist, else just average all 
        g_cnt = min(len(gossips),5)
        return sum(gossips[:g_cnt])/g_cnt

    def decide_torl(self,gossip_heuristic): #decide whether to talk or listen 
        #dunction balance between heuristic and round number 
        #if gossip_heuristic is higher 
        round_num = self.round_number
        thresh_value = 45 
        #right now linear - but may make more logarithmic or exponential 
        #say 100 rounds and there are 
        heuristic = gossip_heuristic

        #to allow for range of 27 cuz acerage of top has a max of about 88
        #once we get a round number 
        #increment = 27/numrounds 
        increment = float(float(7.25)/self.total_rounds)
        #increment = .15 
        #print("the value of the increment is " + str(increment))
        thresh = thresh_value + increment*round_num
        #print("this is the value:" + str(heuristic))
        #print("this is the thresh value:" + str(thresh))'''
        if heuristic > thresh:
            #pick a value 
            #take top 1/3 of scores stored 
            sorted_gossip = self.good_gossips
            top_vals = math.floor(len(sorted_gossip)/5)  #maybe as game goes on we adjust this?
            random_index = random.randint(0, top_vals)
            gossip_return = sorted_gossip[random_index]
            #print("the gossip value player number " + str(self.id) + " is sharing is:" + str(gossip_return))
            return 'talk', gossip_return
        #otherwise generate a ratio of listen to move
        #ideally a split of about 20 speakers, 60 listerns, and 10 movers 
        #rand generate a ratio of 70 and if 10 or less than move, else listen 
        
        '''decision = random.randint(0, 70)
        if decision <= 10:
            return 'move',0'''
        return 'listen',0

        


