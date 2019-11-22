# InformalHearingPresentationTask_Organization

<details><summary>Links for InformalHearingPresentationTask_Organization</summary>

```
digraph G {
rankdir="LR";
"InformalHearingPresentationTask_Organization" -> "InformalHearingPresentationTask_User" [label=8]
"InformalHearingPresentationTask_Organization" -> "JudgeAssignTask_User" [label=7]
"InformalHearingPresentationTask_Organization" -> "BvaDispatchTask_Organization" [label=1]
"InformalHearingPresentationTask_Organization" -> "VeteranRecordRequest_Organization" [label=1]
"DistributionTask_Organization" -> "InformalHearingPresentationTask_Organization" [label=75]
"EvidenceSubmissionWindowTask_Organization" -> "InformalHearingPresentationTask_Organization" [label=9]
"TrackVeteranTask_Organization" -> "InformalHearingPresentationTask_Organization" [label=1]
}
```
</details>

![RTO.DTO.SHTO.HTO-41136](dot/RTO.DTO.SHTO.HTO.dot.png)

## Nextlinks

   * 8 [InformalHearingPresentationTask_User](InformalHearingPresentationTask_User.md)
   * 7 [JudgeAssignTask_User](JudgeAssignTask_User.md)
   * 1 [BvaDispatchTask_Organization](BvaDispatchTask_Organization.md)
   * 1 [VeteranRecordRequest_Organization](VeteranRecordRequest_Organization.md)

## Backlinks

   * 75 [DistributionTask_Organization](DistributionTask_Organization.md)
   * 9 [EvidenceSubmissionWindowTask_Organization](EvidenceSubmissionWindowTask_Organization.md)
   * 1 [TrackVeteranTask_Organization](TrackVeteranTask_Organization.md)

## RTO.TVTO.DTO.IHPTO

75 occurrences (example appeals: [34538, 39812, 41319, 41838, 42495])

<details><summary>PlantUML for 34538</summary>

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

![RTO.TVTO.DTO.IHPTO-34538](uml/RTO.TVTO.DTO.IHPTO-34538.png)

## RTO.TVTO.DTO.ESWTO.IHPTO

9 occurrences (example appeals: [40596, 15370, 42548, 41133, 40540])

<details><summary>PlantUML for 40596</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.TrackVeteranTask_Organization #8da0cb
object 2.DistributionTask_Organization #fc8d62
object 3.EvidenceSubmissionWindowTask_Organization #b3b3b3
object 4.InformalHearingPresentationTask_Organization #ffd92f
0.RootTask_Organization -- 1.TrackVeteranTask_Organization
0.RootTask_Organization -- 2.DistributionTask_Organization
2.DistributionTask_Organization -- 3.EvidenceSubmissionWindowTask_Organization
2.DistributionTask_Organization -- 4.InformalHearingPresentationTask_Organization
@enduml
```
</details>

![RTO.TVTO.DTO.ESWTO.IHPTO-40596](uml/RTO.TVTO.DTO.ESWTO.IHPTO-40596.png)

## RTO.DTO.JATU.JDRTU.ATU.TVTO.IHPTO

1 occurrences (example appeals: [3875])

<details><summary>PlantUML for 3875</summary>

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

![RTO.DTO.JATU.JDRTU.ATU.TVTO.IHPTO-3875](uml/RTO.DTO.JATU.JDRTU.ATU.TVTO.IHPTO-3875.png)

