| [README.md](/README.md) | [Task Listing](tasklist.md) |

# BvaDispatchTask_User

## Tasks Created Before and After

<details><summary>Tasks created before and after BvaDispatchTask_User</summary>

```
digraph G {
rankdir="LR";
"BvaDispatchTask_User" -> "ReturnedUndeliverableCorrespondenceMailTask_Organization" [label=1]
"BvaDispatchTask_Organization" -> "BvaDispatchTask_User" [label=16]
}
```
</details>

![BvaDispatchTask_User](dot/BvaDispatchTask_User.dot.png)

**Before:**

   * [BvaDispatchTask_Organization](BvaDispatchTask_Organization.md): 16 times

**After:**

   * [ReturnedUndeliverableCorrespondenceMailTask_Organization](ReturnedUndeliverableCorrespondenceMailTask_Organization.md): 1 times

## Task Creation Sequences

### RTO.TVTO.DTO.IHPTO.IHPTU.JATU.JDRTU.ATU.BDTO.BDTU

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

![RTO.TVTO.DTO.IHPTO.IHPTU.JATU.JDRTU.ATU.BDTO.BDTU-30234](uml/RTO.TVTO.DTO.IHPTO.IHPTU.JATU.JDRTU.ATU.BDTO.BDTU-30234.png)

### RTO.DTO.JATU.JDRTU.ATU.BDTO.BDTU

3 occurrences (example appeal IDs: [32724, 38039, 40617])

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

![RTO.DTO.JATU.JDRTU.ATU.BDTO.BDTU-32724](uml/RTO.DTO.JATU.JDRTU.ATU.BDTO.BDTU-32724.png)

### RTO.TVTO.DTO.JATU.JDRTU.ATU.BDTO.BDTU

3 occurrences (example appeal IDs: [33346, 41369, 37901])

<details><summary>Task Tree for appeal with ID 33346</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.TrackVeteranTask_Organization #8da0cb
object 2.DistributionTask_Organization #fc8d62
object 3.JudgeAssignTask_User #8da0cb
object 4.JudgeDecisionReviewTask_User #66c2a5
object 5.AttorneyTask_User #fc8d62
object 6.BvaDispatchTask_Organization #e5c494
object 7.BvaDispatchTask_User #e5c494
0.RootTask_Organization -- 1.TrackVeteranTask_Organization
0.RootTask_Organization -- 2.DistributionTask_Organization
0.RootTask_Organization -- 3.JudgeAssignTask_User
0.RootTask_Organization -- 4.JudgeDecisionReviewTask_User
4.JudgeDecisionReviewTask_User -- 5.AttorneyTask_User
0.RootTask_Organization -- 6.BvaDispatchTask_Organization
6.BvaDispatchTask_Organization -- 7.BvaDispatchTask_User
@enduml
```
</details>

![RTO.TVTO.DTO.JATU.JDRTU.ATU.BDTO.BDTU-33346](uml/RTO.TVTO.DTO.JATU.JDRTU.ATU.BDTO.BDTU-33346.png)

### RTO.TVTO.DTO.IHPTO.JATU.JDRTU.ATU.BDTO.BDTU

3 occurrences (example appeal IDs: [34538, 10197, 29665])

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

![RTO.TVTO.DTO.IHPTO.JATU.JDRTU.ATU.BDTO.BDTU-34538](uml/RTO.TVTO.DTO.IHPTO.JATU.JDRTU.ATU.BDTO.BDTU-34538.png)

### RTO.TVTO.DTO.IHPTO.JATU.ICTO.ICTU.THTU.JDRTU.ATU.QRTO.QRTU.BDTO.BDTU

1 occurrences (example appeal IDs: [7729])

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

![RTO.TVTO.DTO.IHPTO.JATU.ICTO.ICTU.THTU.JDRTU.ATU.QRTO.QRTU.BDTO.BDTU-7729](uml/RTO.TVTO.DTO.IHPTO.JATU.ICTO.ICTU.THTU.JDRTU.ATU.QRTO.QRTU.BDTO.BDTU-7729.png)

### RTO.DTO.JATU.JDRTU.ATU.TVTO.IHPTO.BDTO.BDTU

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

![RTO.DTO.JATU.JDRTU.ATU.TVTO.IHPTO.BDTO.BDTU-3875](uml/RTO.DTO.JATU.JDRTU.ATU.TVTO.IHPTO.BDTO.BDTU-3875.png)

### RTO.DTO.EOAMTO.EOAMTO.EOAMTU.JATU.JDRTU.ATU.BDTO.BDTU

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

![RTO.DTO.EOAMTO.EOAMTO.EOAMTU.JATU.JDRTU.ATU.BDTO.BDTU-10213](uml/RTO.DTO.EOAMTO.EOAMTO.EOAMTU.JATU.JDRTU.ATU.BDTO.BDTU-10213.png)

