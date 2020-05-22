 # Turn the Light on 
        self.set_light_on()
        #While the light is on 
        while(self.light_is_on()):
            #AFter for loop finishes goes back to While loop sets light to off. Then back through the for loop, if no swaps made false persists so the while loop breaks
            self.set_light_off()
            #go through all elements in the list
            # for i in range(len(self._list) - 1):

            count = 0
            length = len(self._list) - 1
            print('move right',self.can_move_right())

            while(self.can_move_right()):
                print('postion', self._position)
                print(len(self._list) -1 )
                print('count', count)                
                self.swap_item()
              
                # print('item',self._item)

                
                if (self.compare_item() == 1):
                    self.move_right()
                elif (self.compare_item() == -1):
                    self.swap_item()
                    count += 1
                    self.move_right()
                else:
                    self.move_right()
                    
            while(self.can_move_left()):
                self.move_left()

            
            self.set_light_on()
            print(self._list)

        
        return self._list        

     #################################### first pass ####################################################   

    # def sort(self):
    #     """
    #     Sort the robot's list.
    #     """
    #     # Turn the Light on 
    #     self.set_light_on()

    #     #While the light is on 
    #     while(self._light == "ON"):
    #         #AFter for loop finishes goes back to While loop sets light to off. Then back through the for loop, if no swaps made false persists so the while loop breaks
    #         self.set_light_off()
    #         #go through all elements in the list
    #         for i in range(len(self._list) - 1):
        
    #             if self._list[i] > self._list[i+1]:
            
    #                 temp = self._list[i]
    #                 self._list[i] = self._list[i+1]
    #                 self._list[i+1] = temp
    #                 self.set_light_on()

    #     return self._list


# def bubble_sort(arr):
#     # Your code here
#     has_swapped = True
   
#     while(has_swapped):

#         has_swapped = False

#         for i in range(len(arr) - 1):
            
#             if arr[i] > arr[i+1]:
           
#                 temp = arr[i]
#                 arr[i] = arr[i+1]
#                 arr[i+1] = temp
#                 has_swapped=True

    # return arr