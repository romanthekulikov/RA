import unittest
from Lw6 import TV

'''
coverage report -m
coverage run -m unittest TestClass.py
'''
class TestTV(unittest.TestCase):
    def setUp(self):
        self.TV = TV()

    def test_is_turn_off(self):
        IsOff = self.TV.IsTurnedOn()
        self.assertEqual(IsOff, False, "Incorrect check TV mode off")

    def test_is_turn_on(self):
        self.TV.TurnOn()
        IsOn = self.TV.IsTurnedOn()
        self.assertEqual(IsOn, True, "Incorrect check TV mode on")

    def test_is_turn_off(self):
        self.TV.TurnOn()
        self.TV.TurnOff()
        IsOn = self.TV.IsTurnedOn()
        self.assertEqual(IsOn, False, "Incorrect check TV mode off")

    def test_check_channel_range_when_channel_is_0(self):
        expected_result_0 = False
        channel_0 = 0
        result_0 = self.TV.CheckChannelRange(channel_0)
        self.assertEqual(expected_result_0, result_0, "Incorrect check channel range when channel = 0")

    def test_check_channel_range_when_channel_is_1(self):
        expected_result_1 = True
        channel_1 = 1
        result_1 = self.TV.CheckChannelRange(channel_1)
        self.assertEqual(expected_result_1, result_1, "Incorrect check channel range when channel = 1")
    
    def test_check_channel_range_when_channel_is_10(self):
        expected_result_10 = True
        channel_10 = 10
        result_10 = self.TV.CheckChannelRange(channel_10)
        self.assertEqual(expected_result_10, result_10, "Incorrect check channel range when channel = 10")

    def test_check_channel_range_when_channel_is_11(self):
        expected_result_11 = False
        channel_11 = 11
        result_11 = self.TV.CheckChannelRange(channel_11)
        self.assertEqual(expected_result_11, result_11, "Incorrect check channel range when channel = 11")

    def test_check_get_channel_when_TV_is_off(self):
        expected_channel = 0
        
        actual_channel = self.TV.GetChannel()
        
        self.assertEqual(actual_channel, expected_channel, "Incorrect get channel when TV is off")

    def test_check_get_channel_when_TV_is_on(self):
        expected_channel = {1: "1"}

        self.TV.TurnOn()
        actual_channel = self.TV.GetChannel()
        
        self.assertEqual(actual_channel, expected_channel, "Incorrect get channel when TV is on")

    def test_select_channel_tv_on(self):
        selected_channel = {10: "10"}
        self.TV.TurnOn()
        self.TV.SelectChannel(10)

        result = self.TV.GetChannel()
        
        self.assertEqual(result, selected_channel, "Incorrect selected channel")

    def test_select_channel_tv_off(self):
        expected_result = "TV is off"
        
        result = self.TV.SelectChannel(10)

        self.assertEqual(result, expected_result, "Incorrect selected channel")

    def test_get_list_channel_when_tv_is_on(self):
        expected_result = { 
            1: "1", 
            2: "2", 
            3: "3", 
            4: "4", 
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "10"}
        self.TV.TurnOn()
        result = self.TV.GetListOfChannel()
        self.assertEqual(result, expected_result, "Incorrect get list of channel when tv is on")

    def test_get_list_channel_when_tv_is_off(self):
        expected_result = "TV is off"

        result = self.TV.GetListOfChannel()
        self.assertEqual(result, expected_result, "Incorrect get list of channel when tv is off")

    def test_select_channel_by_name_when_TV_is_off(self):
         expected_result = "TV is off"
         result = self.TV.SelectChannelByName("10")

         self.assertEqual(result, expected_result, "Incorrect select channel by name when TV is off")

    def test_select_channel_by_name_when_TV_is_on(self):
         expected_result = {10: "10"}
         self.TV.TurnOn()
         self.TV.SelectChannelByName("10")
         result = self.TV.GetChannel()
         self.assertEqual(result, expected_result, "Incorrect select channel by name when TV is on")


    def test_select_previous_channel_when_tv_is_off(self):
        expected_result = 0
        self.TV.SelectPreviousChannel()
        result = self.TV.GetChannel()

        self.assertEqual(result, expected_result, "Incorrect select previous channel when TV is off")

    def test_select_previous_channel_when_tv_is_on(self):
        expected_result = {1: "1"}
        self.TV.TurnOn()
        self.TV.SelectChannel(2)
        self.TV.SelectPreviousChannel()
        result = self.TV.GetChannel()

        self.assertEqual(result, expected_result, "Incorrect select previous channel when TV is on")

    def test_select_previous_channel_for_first_channel(self):
        expected_result = {1: "1"}
        self.TV.TurnOn()
        self.TV.SelectPreviousChannel()
        result = self.TV.GetChannel()

        self.assertEqual(result, expected_result, "Incorrect select previous channel when TV is on")
        
if __name__ == '__main__':
    unittest.main()
