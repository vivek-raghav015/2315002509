# Campus Notification System Design

## Objective

The objective of this project is to prioritize campus notifications and display the most important notifications to students.

## Notification Types

1. Placement
2. Result
3. Event

## Priority Logic

Each notification type is assigned a weight:

| Type      | Weight |
| --------- | ------ |
| Placement | 3      |
| Result    | 2      |
| Event     | 1      |

Priority Score Formula:

Priority Score = Type Weight + Recency

More recent notifications receive higher priority.

## Algorithm

1. Read all notifications.
2. Convert timestamp into datetime format.
3. Assign weight according to notification type.
4. Calculate priority score.
5. Sort notifications in descending order.
6. Select top 10 notifications.
7. Display results.

## Data Structure Used

* List of dictionaries
* Dictionary for weights
* Datetime module for timestamp processing

## Complexity

Time Complexity: O(n log n)

Space Complexity: O(n)

## Output

The system displays top priority notifications based on notification type and timestamp.

## Future Improvements

* Database integration
* API integration
* User-specific notifications
* Real-time updates
* Web dashboard
