| [README.md](/README.md) | [Task Listing](tasklist.md) |

# ScheduleHearingTask_Organization

[ScheduleHearingTask_Organization description](../descr/ScheduleHearingTask_Organization.md)

## Tasks Created Before and After

<details><summary>Tasks created before and after ScheduleHearingTask_Organization</summary>

```
digraph G {
rankdir="LR";
"DistributionTask_Organization" -> "ScheduleHearingTask_Organization" [label=129]
"ScheduleHearingTask_Organization" -> "HearingTask_Organization" [label=129]
}
```
</details>

![ScheduleHearingTask_Organization](dot/ScheduleHearingTask_Organization.dot.png)

**Before:**

   * [DistributionTask_Organization](DistributionTask_Organization.md): 129 times

**After:**

   * [HearingTask_Organization](HearingTask_Organization.md): 129 times

## Task Creation Sequences

### RTO.TVTO.DTO.SHTO

[RTO.TVTO.DTO.SHTO description](../descr/RTO.TVTO.DTO.SHTO.md)

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
Organization
}
  object 3.ScheduleHearingTask #a6d854 {
Organization  <back:white>    </back>
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

![RTO.TVTO.DTO.SHTO-16461](uml/RTO.TVTO.DTO.SHTO-16461.png)

### RTO.DTO.SHTO

[RTO.DTO.SHTO description](../descr/RTO.DTO.SHTO.md)

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
Organization
}
  object 2.ScheduleHearingTask #a6d854 {
Organization  <back:white>    </back>
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

![RTO.DTO.SHTO-41136](uml/RTO.DTO.SHTO-41136.png)

