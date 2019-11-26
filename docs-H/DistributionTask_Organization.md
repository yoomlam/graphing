| [README.md](/README.md) | [Task Listing](tasklist.md) |

# DistributionTask_Organization

[DistributionTask_Organization description](../descr/DistributionTask_Organization.md)

## Tasks Created Before and After

<details><summary>Tasks created before and after DistributionTask_Organization</summary>

```
digraph G {
rankdir="LR";
"DistributionTask_Organization" -> "ScheduleHearingTask_Organization" [label=129]
"RootTask_Organization" -> "DistributionTask_Organization" [label=9]
"TrackVeteranTask_Organization" -> "DistributionTask_Organization" [label=120]
}
```
</details>

![DistributionTask_Organization](dot/DistributionTask_Organization.dot.png)

**Before:**

   * [TrackVeteranTask_Organization](TrackVeteranTask_Organization.md): 120 times
   * [RootTask_Organization](RootTask_Organization.md): 9 times

**After:**

   * [ScheduleHearingTask_Organization](ScheduleHearingTask_Organization.md): 129 times

## Task Creation Sequences

### RTO.TVTO.DTO

[RTO.TVTO.DTO description](../descr/RTO.TVTO.DTO.md)

120 occurrences (example appeal IDs: [16461, 42769, 42820, 42010, 42071])

<details><summary>Task Tree for appeal with ID 16461</summary>

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
Organization  <back:white>    </back>
}
  object 3.ScheduleHearingTask #a6d854 {
Organization
}
  object 4.HearingTask #e78ac3 {
Organization
}
0.RootTask -- 1.TrackVeteranTask
0.RootTask -- 2.DistributionTask
4.HearingTask -- 3.ScheduleHearingTask
2.DistributionTask -- 4.HearingTask
@enduml
```
</details>

![RTO.TVTO.DTO-16461](uml/RTO.TVTO.DTO-16461.png)

### RTO.DTO

[RTO.DTO description](../descr/RTO.DTO.md)

9 occurrences (example appeal IDs: [41136, 42097, 4988, 42691, 40835])

<details><summary>Task Tree for appeal with ID 41136</summary>

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
Organization  <back:white>    </back>
}
  object 2.ScheduleHearingTask #a6d854 {
Organization
}
  object 3.HearingTask #e78ac3 {
Organization
}
0.RootTask -- 1.DistributionTask
3.HearingTask -- 2.ScheduleHearingTask
1.DistributionTask -- 3.HearingTask
@enduml
```
</details>

![RTO.DTO-41136](uml/RTO.DTO-41136.png)

