'''
Given a list of different students' scores, write a function that returns the average of each student's top five scores. You should return the averages in ascending order of the students' id numbers.

Each entry (scores[i]) has the student's id number (scores[i][0]) and the student's score (scores[i][1]). The averages should be calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average student `1` is `87`.
The average of student `2` is `88.6`, but with integer division is `88`.


source: codesignal.com (Lambda Challenge)

'''

def csAverageOfTopFive(scores):
    scores_dict = {}
    for score in scores:  # O(n)
        # id will be stored as the key and scores will be stored as a list
        if score[0] not in scores_dict:
            scores_dict[score[0]] = [score[1]]
        else:
            scores_dict[score[0]].append(score[1])

    average_scores = []

    for key, value in scores_dict.items():
        average = 0
        # Since we want the top 5 scores, we have to reverse the list so that the values in the list are descending
        value.sort(reverse=True)
        if(len(value) > 5):
            five_items = value[:5]
            average = sum(five_items) / len(five_items)
        else:
            average = sum(value) // len(value)

        average_scores.append([key, average])

    return average_scores


print(csAverageOfTopFive([[1, 91], [1, 92], [2, 93], [2, 97], [
    1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]))
