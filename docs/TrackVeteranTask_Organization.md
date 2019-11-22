| [README.md](README.md) | [Task Listing](tasklist.md) |

# TrackVeteranTask_Organization

## Tasks Created Before and After

<details><summary>Tasks created before and after TrackVeteranTask_Organization</summary>

```
digraph G {
rankdir="LR";
"DistributionTask_Organization" -> "TrackVeteranTask_Organization" [label=1]
"EvidenceSubmissionWindowTask_Organization" -> "TrackVeteranTask_Organization" [label=2]
"TrackVeteranTask_Organization" -> "TrackVeteranTask_Organization" [label=3]
"RootTask_Organization" -> "TrackVeteranTask_Organization" [label=301]
"TrackVeteranTask_Organization" -> "InformalHearingPresentationTask_Organization" [label=1]
"HearingTask_Organization" -> "TrackVeteranTask_Organization" [label=1]
"TrackVeteranTask_Organization" -> "JudgeAssignTask_User" [label=3]
"AttorneyTask_User" -> "TrackVeteranTask_Organization" [label=1]
"TrackVeteranTask_Organization" -> "DistributionTask_Organization" [label=301]
}
```
</details>

![TrackVeteranTask_Organization](dot/TrackVeteranTask_Organization.dot.png)

**Before:**

   * [RootTask_Organization](RootTask_Organization.md): 301 times
   * [TrackVeteranTask_Organization](TrackVeteranTask_Organization.md): 3 times
   * [EvidenceSubmissionWindowTask_Organization](EvidenceSubmissionWindowTask_Organization.md): 2 times
   * [AttorneyTask_User](AttorneyTask_User.md): 1 times
   * [HearingTask_Organization](HearingTask_Organization.md): 1 times
   * [DistributionTask_Organization](DistributionTask_Organization.md): 1 times

**After:**

   * [DistributionTask_Organization](DistributionTask_Organization.md): 301 times
   * [JudgeAssignTask_User](JudgeAssignTask_User.md): 3 times
   * [TrackVeteranTask_Organization](TrackVeteranTask_Organization.md): 3 times
   * [InformalHearingPresentationTask_Organization](InformalHearingPresentationTask_Organization.md): 1 times

## Task Creation Sequences

### RTO.TVTO

301 occurrences (example appeal IDs: [42769, 34538, 39812, 41319, 40595])

<details><summary>Task Tree for appeal with ID 42769</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.TrackVeteranTask_Organization #8da0cb
object 2.DistributionTask_Organization #fc8d62
object 3.ScheduleHearingTask_Organization #a6d854
object 4.HearingTask_Organization #e78ac3
0.RootTask_Organization -- 1.TrackVeteranTask_Organization
0.RootTask_Organization -- 2.DistributionTask_Organization
4.HearingTask_Organization -- 3.ScheduleHearingTask_Organization
2.DistributionTask_Organization -- 4.HearingTask_Organization
@enduml
```
</details>

![RTO.TVTO-42769](uml/RTO.TVTO-42769.png)

### RTO.TVTO.TVTO

3 occurrences (example appeal IDs: [40894, 42805, 42609])

<details><summary>Task Tree for appeal with ID 40894</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.TrackVeteranTask_Organization #8da0cb
object 2.TrackVeteranTask_Organization #8da0cb
object 3.DistributionTask_Organization #fc8d62
object 4.EvidenceSubmissionWindowTask_Organization #b3b3b3
0.RootTask_Organization -- 1.TrackVeteranTask_Organization
0.RootTask_Organization -- 2.TrackVeteranTask_Organization
0.RootTask_Organization -- 3.DistributionTask_Organization
3.DistributionTask_Organization -- 4.EvidenceSubmissionWindowTask_Organization
@enduml
```
</details>

![RTO.TVTO.TVTO-40894](uml/RTO.TVTO.TVTO-40894.png)

### RTO.DTO.ESWTO.TVTO

2 occurrences (example appeal IDs: [15152, 17948])

<details><summary>Task Tree for appeal with ID 15152</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.DistributionTask_Organization #fc8d62
object 2.EvidenceSubmissionWindowTask_Organization #b3b3b3
object 3.TrackVeteranTask_Organization #8da0cb
object 4.JudgeAssignTask_User #8da0cb
object 5.JudgeDecisionReviewTask_User #66c2a5
object 6.AttorneyTask_User #fc8d62
object 7.JudgeDecisionReviewTask_User #66c2a5
object 8.BvaDispatchTask_Organization #e5c494
object 9.BvaDispatchTask_User #e5c494
0.RootTask_Organization -- 1.DistributionTask_Organization
1.DistributionTask_Organization -- 2.EvidenceSubmissionWindowTask_Organization
0.RootTask_Organization -- 3.TrackVeteranTask_Organization
0.RootTask_Organization -- 4.JudgeAssignTask_User
0.RootTask_Organization -- 5.JudgeDecisionReviewTask_User
5.JudgeDecisionReviewTask_User -- 6.AttorneyTask_User
0.RootTask_Organization -- 7.JudgeDecisionReviewTask_User
0.RootTask_Organization -- 8.BvaDispatchTask_Organization
8.BvaDispatchTask_Organization -- 9.BvaDispatchTask_User
@enduml
```
</details>

![RTO.DTO.ESWTO.TVTO-15152](uml/RTO.DTO.ESWTO.TVTO-15152.png)

### RTO.DTO.JATU.JDRTU.ATU.TVTO

1 occurrences (example appeal IDs: [3875])

<details><summary>Task Tree for appeal with ID 3875</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.DistributionTask_Organization #fc8d62
object 2.JudgeAssignTask_User #8da0cb
object 3.JudgeAssignTask_User #8da0cb
object 4.JudgeDecisionReviewTask_User #66c2a5
object 5.AttorneyTask_User #fc8d62
object 6.TrackVeteranTask_Organization #8da0cb
object 7.InformalHearingPresentationTask_Organization #ffd92f
object 8.BvaDispatchTask_Organization #e5c494
object 9.BvaDispatchTask_User #e5c494
object 10.BvaDispatchTask_User #e5c494
0.RootTask_Organization -- 1.DistributionTask_Organization
0.RootTask_Organization -- 2.JudgeAssignTask_User
0.RootTask_Organization -- 3.JudgeAssignTask_User
0.RootTask_Organization -- 4.JudgeDecisionReviewTask_User
4.JudgeDecisionReviewTask_User -- 5.AttorneyTask_User
0.RootTask_Organization -- 6.TrackVeteranTask_Organization
0.RootTask_Organization -- 7.InformalHearingPresentationTask_Organization
0.RootTask_Organization -- 8.BvaDispatchTask_Organization
8.BvaDispatchTask_Organization -- 9.BvaDispatchTask_User
8.BvaDispatchTask_Organization -- 10.BvaDispatchTask_User
@enduml
```
</details>

![RTO.DTO.JATU.JDRTU.ATU.TVTO-3875](uml/RTO.DTO.JATU.JDRTU.ATU.TVTO-3875.png)

### RTO.DTO.TVTO

1 occurrences (example appeal IDs: [11092])

<details><summary>Task Tree for appeal with ID 11092</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.DistributionTask_Organization #fc8d62
object 2.TrackVeteranTask_Organization #8da0cb
object 3.JudgeAssignTask_User #8da0cb
object 4.JudgeDecisionReviewTask_User #66c2a5
object 5.AttorneyTask_User #fc8d62
0.RootTask_Organization -- 1.DistributionTask_Organization
0.RootTask_Organization -- 2.TrackVeteranTask_Organization
0.RootTask_Organization -- 3.JudgeAssignTask_User
0.RootTask_Organization -- 4.JudgeDecisionReviewTask_User
4.JudgeDecisionReviewTask_User -- 5.AttorneyTask_User
@enduml
```
</details>

![RTO.DTO.TVTO-11092](uml/RTO.DTO.TVTO-11092.png)

### RTO.DTO.SHTO.HTO.TVTO

1 occurrences (example appeal IDs: [4988])

<details><summary>Task Tree for appeal with ID 4988</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.DistributionTask_Organization #fc8d62
object 2.ScheduleHearingTask_Organization #a6d854
object 3.HearingTask_Organization #e78ac3
object 4.TrackVeteranTask_Organization #8da0cb
0.RootTask_Organization -- 1.DistributionTask_Organization
3.HearingTask_Organization -- 2.ScheduleHearingTask_Organization
1.DistributionTask_Organization -- 3.HearingTask_Organization
0.RootTask_Organization -- 4.TrackVeteranTask_Organization
@enduml
```
</details>

![RTO.DTO.SHTO.HTO.TVTO-4988](uml/RTO.DTO.SHTO.HTO.TVTO-4988.png)

