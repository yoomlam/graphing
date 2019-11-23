| [README.md](/README.md) | [Task Listing](tasklist.md) |

# ReturnedUndeliverableCorrespondenceMailTask_Organization

## Tasks Created Before and After

<details><summary>Tasks created before and after ReturnedUndeliverableCorrespondenceMailTask_Organization</summary>

```
digraph G {
rankdir="LR";
"HearingTask_Organization" -> "ReturnedUndeliverableCorrespondenceMailTask_Organization" [label=1]
"BvaDispatchTask_User" -> "ReturnedUndeliverableCorrespondenceMailTask_Organization" [label=3]
"ReturnedUndeliverableCorrespondenceMailTask_Organization" -> "ReturnedUndeliverableCorrespondenceMailTask_Organization" [label=4]
"ReturnedUndeliverableCorrespondenceMailTask_Organization" -> "ReturnedUndeliverableCorrespondenceMailTask_User" [label=3]
}
```
</details>

![ReturnedUndeliverableCorrespondenceMailTask_Organization](dot/ReturnedUndeliverableCorrespondenceMailTask_Organization.dot.png)

**Before:**

   * [ReturnedUndeliverableCorrespondenceMailTask_Organization](ReturnedUndeliverableCorrespondenceMailTask_Organization.md): 4 times
   * [BvaDispatchTask_User](BvaDispatchTask_User.md): 3 times
   * [HearingTask_Organization](HearingTask_Organization.md): 1 times

**After:**

   * [ReturnedUndeliverableCorrespondenceMailTask_Organization](ReturnedUndeliverableCorrespondenceMailTask_Organization.md): 4 times
   * [ReturnedUndeliverableCorrespondenceMailTask_User](ReturnedUndeliverableCorrespondenceMailTask_User.md): 3 times

## Task Creation Sequences

### RTO.TVTO.DTO.IHPTO.JATU.JDRTU.ATU.BDTO.BDTU.RUCMTO

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

![RTO.TVTO.DTO.IHPTO.JATU.JDRTU.ATU.BDTO.BDTU.RUCMTO-29665](uml/RTO.TVTO.DTO.IHPTO.JATU.JDRTU.ATU.BDTO.BDTU.RUCMTO-29665.png)

### RTO.TVTO.DTO.IHPTO.JATU.JDRTU.ATU.BDTO.BDTU.RUCMTO.RUCMTO

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

![RTO.TVTO.DTO.IHPTO.JATU.JDRTU.ATU.BDTO.BDTU.RUCMTO.RUCMTO-29665](uml/RTO.TVTO.DTO.IHPTO.JATU.JDRTU.ATU.BDTO.BDTU.RUCMTO.RUCMTO-29665.png)

### RTO.TVTO.DTO.SHTO.HTO.RUCMTO.RUCMTO

1 occurrences (example appeal IDs: [2056])

<details><summary>Task Tree for appeal with ID 2056</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.TrackVeteranTask_Organization #8da0cb
object 2.DistributionTask_Organization #fc8d62
object 3.ScheduleHearingTask_Organization #a6d854
object 4.HearingTask_Organization #e78ac3
object 5.ReturnedUndeliverableCorrespondenceMailTask_Organization #e78ac3
object 6.ReturnedUndeliverableCorrespondenceMailTask_Organization #e78ac3
0.RootTask_Organization -- 1.TrackVeteranTask_Organization
0.RootTask_Organization -- 2.DistributionTask_Organization
4.HearingTask_Organization -- 3.ScheduleHearingTask_Organization
2.DistributionTask_Organization -- 4.HearingTask_Organization
0.RootTask_Organization -- 5.ReturnedUndeliverableCorrespondenceMailTask_Organization
5.ReturnedUndeliverableCorrespondenceMailTask_Organization -- 6.ReturnedUndeliverableCorrespondenceMailTask_Organization
@enduml
```
</details>

![RTO.TVTO.DTO.SHTO.HTO.RUCMTO.RUCMTO-2056](uml/RTO.TVTO.DTO.SHTO.HTO.RUCMTO.RUCMTO-2056.png)

### RTO.TVTO.DTO.SHTO.HTO.RUCMTO

1 occurrences (example appeal IDs: [2056])

<details><summary>Task Tree for appeal with ID 2056</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.TrackVeteranTask_Organization #8da0cb
object 2.DistributionTask_Organization #fc8d62
object 3.ScheduleHearingTask_Organization #a6d854
object 4.HearingTask_Organization #e78ac3
object 5.ReturnedUndeliverableCorrespondenceMailTask_Organization #e78ac3
object 6.ReturnedUndeliverableCorrespondenceMailTask_Organization #e78ac3
0.RootTask_Organization -- 1.TrackVeteranTask_Organization
0.RootTask_Organization -- 2.DistributionTask_Organization
4.HearingTask_Organization -- 3.ScheduleHearingTask_Organization
2.DistributionTask_Organization -- 4.HearingTask_Organization
0.RootTask_Organization -- 5.ReturnedUndeliverableCorrespondenceMailTask_Organization
5.ReturnedUndeliverableCorrespondenceMailTask_Organization -- 6.ReturnedUndeliverableCorrespondenceMailTask_Organization
@enduml
```
</details>

![RTO.TVTO.DTO.SHTO.HTO.RUCMTO-2056](uml/RTO.TVTO.DTO.SHTO.HTO.RUCMTO-2056.png)

