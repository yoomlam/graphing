| [README.md](/README.md) | [Task Listing](tasklist.md) |

# DistributionTask_Organization

## Tasks Created Before and After

<details><summary>Tasks created before and after DistributionTask_Organization</summary>

```
digraph G {
rankdir="LR";
"DistributionTask_Organization" -> "TrackVeteranTask_Organization" [label=1]
"DistributionTask_Organization" -> "JudgeAssignTask_User" [label=16]
"DistributionTask_Organization" -> "EvidenceOrArgumentMailTask_Organization" [label=1]
"TrackVeteranTask_Organization" -> "DistributionTask_Organization" [label=116]
"DistributionTask_Organization" -> "SpecialCaseMovementTask_User" [label=1]
"DistributionTask_Organization" -> "InformalHearingPresentationTask_Organization" [label=75]
"RootTask_Organization" -> "DistributionTask_Organization" [label=56]
"DistributionTask_Organization" -> "TranslationTask_Organization" [label=1]
}
```
</details>

![DistributionTask_Organization](dot/DistributionTask_Organization.dot.png)

**Before:**

   * [TrackVeteranTask_Organization](TrackVeteranTask_Organization.md): 116 times
   * [RootTask_Organization](RootTask_Organization.md): 56 times

**After:**

   * [InformalHearingPresentationTask_Organization](InformalHearingPresentationTask_Organization.md): 75 times
   * [JudgeAssignTask_User](JudgeAssignTask_User.md): 16 times
   * [EvidenceOrArgumentMailTask_Organization](EvidenceOrArgumentMailTask_Organization.md): 1 times
   * [TranslationTask_Organization](TranslationTask_Organization.md): 1 times
   * [SpecialCaseMovementTask_User](SpecialCaseMovementTask_User.md): 1 times
   * [TrackVeteranTask_Organization](TrackVeteranTask_Organization.md): 1 times

## Task Creation Sequences

### RTO.TVTO.DTO

116 occurrences (example appeal IDs: [34538, 39812, 41319, 40595, 42034])

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

![RTO.TVTO.DTO-34538](uml/RTO.TVTO.DTO-34538.png)

### RTO.DTO

56 occurrences (example appeal IDs: [32724, 10213, 39837, 41094, 41199])

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

![RTO.DTO-32724](uml/RTO.DTO-32724.png)

### DTO

3 occurrences (example appeal IDs: [6702, 41852, 10958])

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

![DTO-6702](uml/DTO-6702.png)

