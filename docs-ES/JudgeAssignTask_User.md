| [README.md](/README.md) | [Task Listing](tasklist.md) |

# JudgeAssignTask_User

[JudgeAssignTask_User description](../descr/JudgeAssignTask_User.md)

## Tasks Created Before and After

<details><summary>Tasks created before and after JudgeAssignTask_User</summary>

```
digraph G {
rankdir="LR";
"JudgeAssignTask_User" -> "JudgeDecisionReviewTask_User" [label=7]
"InformalHearingPresentationTask_User" -> "JudgeAssignTask_User" [label=2]
"TrackVeteranTask_Organization" -> "JudgeAssignTask_User" [label=2]
"EvidenceSubmissionWindowTask_Organization" -> "JudgeAssignTask_User" [label=2]
"SpecialCaseMovementTask_User" -> "JudgeAssignTask_User" [label=1]
"InformalHearingPresentationTask_Organization" -> "JudgeAssignTask_User" [label=1]
"JudgeAssignTask_User" -> "AttorneyTask_User" [label=1]
}
```
</details>

![JudgeAssignTask_User](dot/JudgeAssignTask_User.dot.png)

**Before:**

   * [TrackVeteranTask_Organization](TrackVeteranTask_Organization.md): 2 times
   * [InformalHearingPresentationTask_User](InformalHearingPresentationTask_User.md): 2 times
   * [EvidenceSubmissionWindowTask_Organization](EvidenceSubmissionWindowTask_Organization.md): 2 times
   * [SpecialCaseMovementTask_User](SpecialCaseMovementTask_User.md): 1 times
   * [InformalHearingPresentationTask_Organization](InformalHearingPresentationTask_Organization.md): 1 times

**After:**

   * [JudgeDecisionReviewTask_User](JudgeDecisionReviewTask_User.md): 7 times
   * [AttorneyTask_User](AttorneyTask_User.md): 1 times

## Task Creation Sequences

### RTO.DTO.ESWTO.TVTO.JATU

[RTO.DTO.ESWTO.TVTO.JATU description](../descr/RTO.DTO.ESWTO.TVTO.JATU.md)

2 occurrences (example appeal IDs: [15152, 17948])

<details><summary>Task Tree for appeal with ID 15152</summary>

```
@startuml
skinparam {
  ObjectBorderColor #555
  ObjectBorderThickness 0
  ObjectFontStyle bold
  ObjectFontSize 14
  ObjectAttributeFontColor #333
  ObjectAttributeFontSize 12
}
  object 0.RootTask #66c2a5 {
Organization
}
  object 1.DistributionTask #fc8d62 {
Organization
}
  object 2.EvidenceSubmissionWindowTask #b3b3b3 {
Organization
}
  object 3.TrackVeteranTask #8da0cb {
Organization
}
  object 4.JudgeAssignTask #8da0cb {
User  <back:white>    </back>
}
  object 5.JudgeDecisionReviewTask #66c2a5 {
User
}
  object 6.AttorneyTask #fc8d62 {
User
}
  object 7.JudgeDecisionReviewTask #66c2a5 {
User
}
  object 8.BvaDispatchTask #e5c494 {
Organization
}
  object 9.BvaDispatchTask #e5c494 {
User
}
0.RootTask -- 1.DistributionTask
1.DistributionTask -- 2.EvidenceSubmissionWindowTask
0.RootTask -- 3.TrackVeteranTask
0.RootTask -- 4.JudgeAssignTask
0.RootTask -- 5.JudgeDecisionReviewTask
5.JudgeDecisionReviewTask -- 6.AttorneyTask
0.RootTask -- 7.JudgeDecisionReviewTask
0.RootTask -- 8.BvaDispatchTask
8.BvaDispatchTask -- 9.BvaDispatchTask
@enduml
```
</details>

![RTO.DTO.ESWTO.TVTO.JATU-15152](uml/RTO.DTO.ESWTO.TVTO.JATU-15152.png)

### RTO.TVTO.DTO.ESWTO.IHPTO.IHPTU.JATU

[RTO.TVTO.DTO.ESWTO.IHPTO.IHPTU.JATU description](../descr/RTO.TVTO.DTO.ESWTO.IHPTO.IHPTU.JATU.md)

2 occurrences (example appeal IDs: [15370, 41412])

<details><summary>Task Tree for appeal with ID 15370</summary>

```
@startuml
skinparam {
  ObjectBorderColor #555
  ObjectBorderThickness 0
  ObjectFontStyle bold
  ObjectFontSize 14
  ObjectAttributeFontColor #333
  ObjectAttributeFontSize 12
}
  object 0.RootTask #66c2a5 {
Organization
}
  object 1.TrackVeteranTask #8da0cb {
Organization
}
  object 2.DistributionTask #fc8d62 {
Organization
}
  object 3.EvidenceSubmissionWindowTask #b3b3b3 {
Organization
}
  object 4.InformalHearingPresentationTask #ffd92f {
Organization
}
  object 5.InformalHearingPresentationTask #ffd92f {
User
}
  object 6.JudgeAssignTask #8da0cb {
User  <back:white>    </back>
}
  object 7.JudgeDecisionReviewTask #66c2a5 {
User
}
  object 8.AttorneyTask #fc8d62 {
User
}
  object 9.BvaDispatchTask #e5c494 {
Organization
}
  object 10.BvaDispatchTask #e5c494 {
User
}
0.RootTask -- 1.TrackVeteranTask
0.RootTask -- 2.DistributionTask
2.DistributionTask -- 3.EvidenceSubmissionWindowTask
2.DistributionTask -- 4.InformalHearingPresentationTask
4.InformalHearingPresentationTask -- 5.InformalHearingPresentationTask
0.RootTask -- 6.JudgeAssignTask
0.RootTask -- 7.JudgeDecisionReviewTask
7.JudgeDecisionReviewTask -- 8.AttorneyTask
0.RootTask -- 9.BvaDispatchTask
9.BvaDispatchTask -- 10.BvaDispatchTask
@enduml
```
</details>

![RTO.TVTO.DTO.ESWTO.IHPTO.IHPTU.JATU-15370](uml/RTO.TVTO.DTO.ESWTO.IHPTO.IHPTU.JATU-15370.png)

### RTO.TVTO.DTO.ESWTO.JATU

[RTO.TVTO.DTO.ESWTO.JATU description](../descr/RTO.TVTO.DTO.ESWTO.JATU.md)

2 occurrences (example appeal IDs: [15411, 40893])

<details><summary>Task Tree for appeal with ID 15411</summary>

```
@startuml
skinparam {
  ObjectBorderColor #555
  ObjectBorderThickness 0
  ObjectFontStyle bold
  ObjectFontSize 14
  ObjectAttributeFontColor #333
  ObjectAttributeFontSize 12
}
  object 0.RootTask #66c2a5 {
Organization
}
  object 1.TrackVeteranTask #8da0cb {
Organization
}
  object 2.DistributionTask #fc8d62 {
Organization
}
  object 3.EvidenceSubmissionWindowTask #b3b3b3 {
Organization
}
  object 4.JudgeAssignTask #8da0cb {
User  <back:white>    </back>
}
  object 5.JudgeDecisionReviewTask #66c2a5 {
User
}
  object 6.AttorneyTask #fc8d62 {
User
}
  object 7.QualityReviewTask #fc8d62 {
Organization
}
  object 8.QualityReviewTask #fc8d62 {
User
}
  object 9.JudgeQualityReviewTask #ffd92f {
User
}
  object 10.BvaDispatchTask #e5c494 {
Organization
}
  object 11.BvaDispatchTask #e5c494 {
User
}
  object 12.BvaDispatchTask #e5c494 {
User
}
  object 13.JudgeDispatchReturnTask #fc8d62 {
User
}
  object 14.JudgeDispatchReturnTask #fc8d62 {
User
}
0.RootTask -- 1.TrackVeteranTask
0.RootTask -- 2.DistributionTask
2.DistributionTask -- 3.EvidenceSubmissionWindowTask
0.RootTask -- 4.JudgeAssignTask
0.RootTask -- 5.JudgeDecisionReviewTask
5.JudgeDecisionReviewTask -- 6.AttorneyTask
0.RootTask -- 7.QualityReviewTask
7.QualityReviewTask -- 8.QualityReviewTask
8.QualityReviewTask -- 9.JudgeQualityReviewTask
0.RootTask -- 10.BvaDispatchTask
10.BvaDispatchTask -- 11.BvaDispatchTask
10.BvaDispatchTask -- 12.BvaDispatchTask
12.BvaDispatchTask -- 13.JudgeDispatchReturnTask
12.BvaDispatchTask -- 14.JudgeDispatchReturnTask
@enduml
```
</details>

![RTO.TVTO.DTO.ESWTO.JATU-15411](uml/RTO.TVTO.DTO.ESWTO.JATU-15411.png)

### RTO.TVTO.DTO.ESWTO.IHPTO.JATU

[RTO.TVTO.DTO.ESWTO.IHPTO.JATU description](../descr/RTO.TVTO.DTO.ESWTO.IHPTO.JATU.md)

1 occurrences (example appeal IDs: [11522])

<details><summary>Task Tree for appeal with ID 11522</summary>

```
@startuml
skinparam {
  ObjectBorderColor #555
  ObjectBorderThickness 0
  ObjectFontStyle bold
  ObjectFontSize 14
  ObjectAttributeFontColor #333
  ObjectAttributeFontSize 12
}
  object 0.RootTask #66c2a5 {
Organization
}
  object 1.TrackVeteranTask #8da0cb {
Organization
}
  object 2.DistributionTask #fc8d62 {
Organization
}
  object 3.EvidenceSubmissionWindowTask #b3b3b3 {
Organization
}
  object 4.InformalHearingPresentationTask #ffd92f {
Organization
}
  object 5.JudgeAssignTask #8da0cb {
User  <back:white>    </back>
}
  object 6.JudgeDecisionReviewTask #66c2a5 {
User
}
  object 7.AttorneyTask #fc8d62 {
User
}
  object 8.AttorneyRewriteTask #8da0cb {
User
}
  object 9.BvaDispatchTask #e5c494 {
Organization
}
  object 10.BvaDispatchTask #e5c494 {
User
}
0.RootTask -- 1.TrackVeteranTask
0.RootTask -- 2.DistributionTask
2.DistributionTask -- 3.EvidenceSubmissionWindowTask
2.DistributionTask -- 4.InformalHearingPresentationTask
0.RootTask -- 5.JudgeAssignTask
0.RootTask -- 6.JudgeDecisionReviewTask
6.JudgeDecisionReviewTask -- 7.AttorneyTask
6.JudgeDecisionReviewTask -- 8.AttorneyRewriteTask
0.RootTask -- 9.BvaDispatchTask
9.BvaDispatchTask -- 10.BvaDispatchTask
@enduml
```
</details>

![RTO.TVTO.DTO.ESWTO.IHPTO.JATU-11522](uml/RTO.TVTO.DTO.ESWTO.IHPTO.JATU-11522.png)

### RTO.DTO.ESWTO.SCMTU.JATU

[RTO.DTO.ESWTO.SCMTU.JATU description](../descr/RTO.DTO.ESWTO.SCMTU.JATU.md)

1 occurrences (example appeal IDs: [40605])

<details><summary>Task Tree for appeal with ID 40605</summary>

```
@startuml
skinparam {
  ObjectBorderColor #555
  ObjectBorderThickness 0
  ObjectFontStyle bold
  ObjectFontSize 14
  ObjectAttributeFontColor #333
  ObjectAttributeFontSize 12
}
  object 0.RootTask #66c2a5 {
Organization
}
  object 1.DistributionTask #fc8d62 {
Organization
}
  object 2.EvidenceSubmissionWindowTask #b3b3b3 {
Organization
}
  object 3.SpecialCaseMovementTask #66c2a5 {
User
}
  object 4.JudgeAssignTask #8da0cb {
User  <back:white>    </back>
}
  object 5.JudgeDecisionReviewTask #66c2a5 {
User
}
  object 6.AttorneyTask #fc8d62 {
User
}
  object 7.AttorneyRewriteTask #8da0cb {
User
}
  object 8.BvaDispatchTask #e5c494 {
Organization
}
  object 9.BvaDispatchTask #e5c494 {
User
}
0.RootTask -- 1.DistributionTask
1.DistributionTask -- 2.EvidenceSubmissionWindowTask
1.DistributionTask -- 3.SpecialCaseMovementTask
0.RootTask -- 4.JudgeAssignTask
0.RootTask -- 5.JudgeDecisionReviewTask
5.JudgeDecisionReviewTask -- 6.AttorneyTask
5.JudgeDecisionReviewTask -- 7.AttorneyRewriteTask
0.RootTask -- 8.BvaDispatchTask
8.BvaDispatchTask -- 9.BvaDispatchTask
@enduml
```
</details>

![RTO.DTO.ESWTO.SCMTU.JATU-40605](uml/RTO.DTO.ESWTO.SCMTU.JATU-40605.png)

