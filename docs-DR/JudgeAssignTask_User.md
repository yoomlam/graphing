| [README.md](/README.md) | [Task Listing](tasklist.md) |

# JudgeAssignTask_User

## Tasks Created Before and After

<details><summary>Tasks created before and after JudgeAssignTask_User</summary>

```
digraph G {
rankdir="LR";
"TrackVeteranTask_Organization" -> "JudgeAssignTask_User" [label=1]
"InformalHearingPresentationTask_Organization" -> "JudgeAssignTask_User" [label=6]
"DistributionTask_Organization" -> "JudgeAssignTask_User" [label=16]
"InformalHearingPresentationTask_User" -> "JudgeAssignTask_User" [label=4]
"EvidenceOrArgumentMailTask_User" -> "JudgeAssignTask_User" [label=1]
"SpecialCaseMovementTask_User" -> "JudgeAssignTask_User" [label=1]
"JudgeAssignTask_User" -> "IhpColocatedTask_Organization" [label=1]
"JudgeAssignTask_User" -> "JudgeDecisionReviewTask_User" [label=21]
}
```
</details>

![JudgeAssignTask_User](dot/JudgeAssignTask_User.dot.png)

**Before:**

   * [DistributionTask_Organization](DistributionTask_Organization.md): 16 times
   * [InformalHearingPresentationTask_Organization](InformalHearingPresentationTask_Organization.md): 6 times
   * [InformalHearingPresentationTask_User](InformalHearingPresentationTask_User.md): 4 times
   * [EvidenceOrArgumentMailTask_User](EvidenceOrArgumentMailTask_User.md): 1 times
   * [SpecialCaseMovementTask_User](SpecialCaseMovementTask_User.md): 1 times
   * [TrackVeteranTask_Organization](TrackVeteranTask_Organization.md): 1 times

**After:**

   * [JudgeDecisionReviewTask_User](JudgeDecisionReviewTask_User.md): 21 times
   * [IhpColocatedTask_Organization](IhpColocatedTask_Organization.md): 1 times

## Task Creation Sequences

### RTO.DTO.JATU

8 occurrences (example appeal IDs: [32724, 38039, 40828, 3875, 40611])

<details><summary>Task Tree for appeal with ID 32724</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.DistributionTask_Organization #fc8d62
object 2.JudgeAssignTask_User #8da0cb
object 3.JudgeDecisionReviewTask_User #66c2a5
object 4.AttorneyTask_User #fc8d62
object 5.BvaDispatchTask_Organization #e5c494
object 6.BvaDispatchTask_User #e5c494
0.RootTask_Organization -- 1.DistributionTask_Organization
0.RootTask_Organization -- 2.JudgeAssignTask_User
0.RootTask_Organization -- 3.JudgeDecisionReviewTask_User
3.JudgeDecisionReviewTask_User -- 4.AttorneyTask_User
0.RootTask_Organization -- 5.BvaDispatchTask_Organization
5.BvaDispatchTask_Organization -- 6.BvaDispatchTask_User
@enduml
```
</details>

![RTO.DTO.JATU-32724](uml/RTO.DTO.JATU-32724.png)

### RTO.TVTO.DTO.JATU

6 occurrences (example appeal IDs: [40595, 33346, 41369, 37901, 40892])

<details><summary>Task Tree for appeal with ID 40595</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.TrackVeteranTask_Organization #8da0cb
object 2.DistributionTask_Organization #fc8d62
object 3.JudgeAssignTask_User #8da0cb
object 4.JudgeDecisionReviewTask_User #66c2a5
object 5.AttorneyTask_User #fc8d62
0.RootTask_Organization -- 1.TrackVeteranTask_Organization
0.RootTask_Organization -- 2.DistributionTask_Organization
0.RootTask_Organization -- 3.JudgeAssignTask_User
0.RootTask_Organization -- 4.JudgeDecisionReviewTask_User
4.JudgeDecisionReviewTask_User -- 5.AttorneyTask_User
@enduml
```
</details>

![RTO.TVTO.DTO.JATU-40595](uml/RTO.TVTO.DTO.JATU-40595.png)

### RTO.TVTO.DTO.IHPTO.JATU

6 occurrences (example appeal IDs: [34538, 39812, 10197, 39823, 7729])

<details><summary>Task Tree for appeal with ID 34538</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.TrackVeteranTask_Organization #8da0cb
object 2.DistributionTask_Organization #fc8d62
object 3.InformalHearingPresentationTask_Organization #ffd92f
object 4.JudgeAssignTask_User #8da0cb
object 5.JudgeDecisionReviewTask_User #66c2a5
object 6.AttorneyTask_User #fc8d62
object 7.BvaDispatchTask_Organization #e5c494
object 8.BvaDispatchTask_User #e5c494
object 9.BvaDispatchTask_User #e5c494
object 10.BvaDispatchTask_User #e5c494
0.RootTask_Organization -- 1.TrackVeteranTask_Organization
0.RootTask_Organization -- 2.DistributionTask_Organization
2.DistributionTask_Organization -- 3.InformalHearingPresentationTask_Organization
0.RootTask_Organization -- 4.JudgeAssignTask_User
0.RootTask_Organization -- 5.JudgeDecisionReviewTask_User
5.JudgeDecisionReviewTask_User -- 6.AttorneyTask_User
0.RootTask_Organization -- 7.BvaDispatchTask_Organization
7.BvaDispatchTask_Organization -- 8.BvaDispatchTask_User
7.BvaDispatchTask_Organization -- 9.BvaDispatchTask_User
7.BvaDispatchTask_Organization -- 10.BvaDispatchTask_User
@enduml
```
</details>

![RTO.TVTO.DTO.IHPTO.JATU-34538](uml/RTO.TVTO.DTO.IHPTO.JATU-34538.png)

### RTO.TVTO.DTO.IHPTO.IHPTU.JATU

4 occurrences (example appeal IDs: [30234, 35142, 5529, 34472])

<details><summary>Task Tree for appeal with ID 30234</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.TrackVeteranTask_Organization #8da0cb
object 2.DistributionTask_Organization #fc8d62
object 3.InformalHearingPresentationTask_Organization #ffd92f
object 4.InformalHearingPresentationTask_User #ffd92f
object 5.JudgeAssignTask_User #8da0cb
object 6.JudgeDecisionReviewTask_User #66c2a5
object 7.AttorneyTask_User #fc8d62
object 8.BvaDispatchTask_Organization #e5c494
object 9.BvaDispatchTask_User #e5c494
0.RootTask_Organization -- 1.TrackVeteranTask_Organization
0.RootTask_Organization -- 2.DistributionTask_Organization
2.DistributionTask_Organization -- 3.InformalHearingPresentationTask_Organization
3.InformalHearingPresentationTask_Organization -- 4.InformalHearingPresentationTask_User
0.RootTask_Organization -- 5.JudgeAssignTask_User
0.RootTask_Organization -- 6.JudgeDecisionReviewTask_User
6.JudgeDecisionReviewTask_User -- 7.AttorneyTask_User
0.RootTask_Organization -- 8.BvaDispatchTask_Organization
8.BvaDispatchTask_Organization -- 9.BvaDispatchTask_User
@enduml
```
</details>

![RTO.TVTO.DTO.IHPTO.IHPTU.JATU-30234](uml/RTO.TVTO.DTO.IHPTO.IHPTU.JATU-30234.png)

### DTO.JATU

2 occurrences (example appeal IDs: [6702, 10958])

<details><summary>Task Tree for appeal with ID 6702</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.TrackVeteranTask_Organization #8da0cb
object 2.DistributionTask_Organization #fc8d62
object 3.JudgeAssignTask_User #8da0cb
object 4.JudgeDecisionReviewTask_User #66c2a5
object 5.AttorneyTask_User #fc8d62
object 6.OtherColocatedTask_Organization #fc8d62
object 7.OtherColocatedTask_User #fc8d62
0.RootTask_Organization -- 1.TrackVeteranTask_Organization
0.RootTask_Organization -- 2.DistributionTask_Organization
0.RootTask_Organization -- 3.JudgeAssignTask_User
0.RootTask_Organization -- 4.JudgeDecisionReviewTask_User
4.JudgeDecisionReviewTask_User -- 5.AttorneyTask_User
5.AttorneyTask_User -- 6.OtherColocatedTask_Organization
6.OtherColocatedTask_Organization -- 7.OtherColocatedTask_User
@enduml
```
</details>

![DTO.JATU-6702](uml/DTO.JATU-6702.png)

### RTO.DTO.EOAMTO.EOAMTO.EOAMTU.JATU

1 occurrences (example appeal IDs: [10213])

<details><summary>Task Tree for appeal with ID 10213</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.DistributionTask_Organization #fc8d62
object 2.EvidenceOrArgumentMailTask_Organization #ffd92f
object 3.EvidenceOrArgumentMailTask_Organization #ffd92f
object 4.EvidenceOrArgumentMailTask_User #ffd92f
object 5.JudgeAssignTask_User #8da0cb
object 6.JudgeDecisionReviewTask_User #66c2a5
object 7.AttorneyTask_User #fc8d62
object 8.BvaDispatchTask_Organization #e5c494
object 9.BvaDispatchTask_User #e5c494
0.RootTask_Organization -- 1.DistributionTask_Organization
0.RootTask_Organization -- 2.EvidenceOrArgumentMailTask_Organization
2.EvidenceOrArgumentMailTask_Organization -- 3.EvidenceOrArgumentMailTask_Organization
3.EvidenceOrArgumentMailTask_Organization -- 4.EvidenceOrArgumentMailTask_User
0.RootTask_Organization -- 5.JudgeAssignTask_User
0.RootTask_Organization -- 6.JudgeDecisionReviewTask_User
6.JudgeDecisionReviewTask_User -- 7.AttorneyTask_User
0.RootTask_Organization -- 8.BvaDispatchTask_Organization
8.BvaDispatchTask_Organization -- 9.BvaDispatchTask_User
@enduml
```
</details>

![RTO.DTO.EOAMTO.EOAMTO.EOAMTU.JATU-10213](uml/RTO.DTO.EOAMTO.EOAMTO.EOAMTU.JATU-10213.png)

### RTO.DTO.SCMTU.JATU

1 occurrences (example appeal IDs: [41963])

<details><summary>Task Tree for appeal with ID 41963</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.DistributionTask_Organization #fc8d62
object 2.SpecialCaseMovementTask_User #a6d854
object 3.JudgeAssignTask_User #8da0cb
0.RootTask_Organization -- 1.DistributionTask_Organization
1.DistributionTask_Organization -- 2.SpecialCaseMovementTask_User
0.RootTask_Organization -- 3.JudgeAssignTask_User
@enduml
```
</details>

![RTO.DTO.SCMTU.JATU-41963](uml/RTO.DTO.SCMTU.JATU-41963.png)

### RTO.DTO.TVTO.JATU

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

![RTO.DTO.TVTO.JATU-11092](uml/RTO.DTO.TVTO.JATU-11092.png)

