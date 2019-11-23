| [README.md](/README.md) | [Task Listing](tasklist.md) |

# ReturnedUndeliverableCorrespondenceMailTask_User

## Tasks Created Before and After

<details><summary>Tasks created before and after ReturnedUndeliverableCorrespondenceMailTask_User</summary>

```
digraph G {
rankdir="LR";
"ReturnedUndeliverableCorrespondenceMailTask_User" -> "Task_Organization" [label=3]
"ReturnedUndeliverableCorrespondenceMailTask_Organization" -> "ReturnedUndeliverableCorrespondenceMailTask_User" [label=3]
}
```
</details>

![ReturnedUndeliverableCorrespondenceMailTask_User](dot/ReturnedUndeliverableCorrespondenceMailTask_User.dot.png)

**Before:**

   * [ReturnedUndeliverableCorrespondenceMailTask_Organization](ReturnedUndeliverableCorrespondenceMailTask_Organization.md): 3 times

**After:**

   * [Task_Organization](Task_Organization.md): 3 times

## Task Creation Sequences

### RTO.TVTO.DTO.IHPTO.JATU.JDRTU.ATU.BDTO.BDTU.RUCMTO.RUCMTO.RUCMTU

3 occurrences (example appeal IDs: [29665, 29665, 29665])

<details><summary>Task Tree for appeal with ID 29665</summary>

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
object 9.ReturnedUndeliverableCorrespondenceMailTask_Organization #e78ac3
object 10.ReturnedUndeliverableCorrespondenceMailTask_Organization #e78ac3
object 11.ReturnedUndeliverableCorrespondenceMailTask_User #e78ac3
object 12.Task_Organization #e78ac3
0.RootTask_Organization -- 1.TrackVeteranTask_Organization
0.RootTask_Organization -- 2.DistributionTask_Organization
2.DistributionTask_Organization -- 3.InformalHearingPresentationTask_Organization
0.RootTask_Organization -- 4.JudgeAssignTask_User
0.RootTask_Organization -- 5.JudgeDecisionReviewTask_User
5.JudgeDecisionReviewTask_User -- 6.AttorneyTask_User
0.RootTask_Organization -- 7.BvaDispatchTask_Organization
7.BvaDispatchTask_Organization -- 8.BvaDispatchTask_User
0.RootTask_Organization -- 9.ReturnedUndeliverableCorrespondenceMailTask_Organization
9.ReturnedUndeliverableCorrespondenceMailTask_Organization -- 10.ReturnedUndeliverableCorrespondenceMailTask_Organization
10.ReturnedUndeliverableCorrespondenceMailTask_Organization -- 11.ReturnedUndeliverableCorrespondenceMailTask_User
11.ReturnedUndeliverableCorrespondenceMailTask_User -- 12.Task_Organization
@enduml
```
</details>

![RTO.TVTO.DTO.IHPTO.JATU.JDRTU.ATU.BDTO.BDTU.RUCMTO.RUCMTO.RUCMTU-29665](uml/RTO.TVTO.DTO.IHPTO.JATU.JDRTU.ATU.BDTO.BDTU.RUCMTO.RUCMTO.RUCMTU-29665.png)

