| [README.md](/README.md) | [Task Listing](tasklist.md) |

# IhpColocatedTask_User

## Tasks Created Before and After

<details><summary>Tasks created before and after IhpColocatedTask_User</summary>

```
digraph G {
rankdir="LR";
"IhpColocatedTask_User" -> "TimedHoldTask_User" [label=3]
"IhpColocatedTask_Organization" -> "IhpColocatedTask_User" [label=3]
}
```
</details>

![IhpColocatedTask_User](dot/IhpColocatedTask_User.dot.png)

**Before:**

   * [IhpColocatedTask_Organization](IhpColocatedTask_Organization.md): 3 times

**After:**

   * [TimedHoldTask_User](TimedHoldTask_User.md): 3 times

## Task Creation Sequences

### RTO.TVTO.DTO.IHPTO.JATU.ICTO.ICTU

3 occurrences (example appeal IDs: [7729, 7729, 7729])

<details><summary>Task Tree for appeal with ID 7729</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.TrackVeteranTask_Organization #8da0cb
object 2.DistributionTask_Organization #fc8d62
object 3.InformalHearingPresentationTask_Organization #ffd92f
object 4.InformalHearingPresentationTask_User #ffd92f
object 5.JudgeAssignTask_User #8da0cb
object 6.IhpColocatedTask_Organization #a6d854
object 7.IhpColocatedTask_User #a6d854
object 8.TimedHoldTask_User #e78ac3
object 9.JudgeDecisionReviewTask_User #66c2a5
object 10.AttorneyTask_User #fc8d62
object 11.QualityReviewTask_Organization #66c2a5
object 12.QualityReviewTask_User #66c2a5
object 13.BvaDispatchTask_Organization #e5c494
object 14.BvaDispatchTask_User #e5c494
0.RootTask_Organization -- 1.TrackVeteranTask_Organization
0.RootTask_Organization -- 2.DistributionTask_Organization
2.DistributionTask_Organization -- 3.InformalHearingPresentationTask_Organization
3.InformalHearingPresentationTask_Organization -- 4.InformalHearingPresentationTask_User
0.RootTask_Organization -- 5.JudgeAssignTask_User
5.JudgeAssignTask_User -- 6.IhpColocatedTask_Organization
6.IhpColocatedTask_Organization -- 7.IhpColocatedTask_User
7.IhpColocatedTask_User -- 8.TimedHoldTask_User
0.RootTask_Organization -- 9.JudgeDecisionReviewTask_User
9.JudgeDecisionReviewTask_User -- 10.AttorneyTask_User
0.RootTask_Organization -- 11.QualityReviewTask_Organization
11.QualityReviewTask_Organization -- 12.QualityReviewTask_User
0.RootTask_Organization -- 13.BvaDispatchTask_Organization
13.BvaDispatchTask_Organization -- 14.BvaDispatchTask_User
@enduml
```
</details>

![RTO.TVTO.DTO.IHPTO.JATU.ICTO.ICTU-7729](uml/RTO.TVTO.DTO.IHPTO.JATU.ICTO.ICTU-7729.png)

