# Implementation dependency graph

Plan P6-r2. The full [task DAG](dependency-graph.mmd) has 127 nodes; [topological order](task-order.json) is authoritative data derived from the manifest. Every edge consumes the predecessor's versioned boundary and acceptance evidence, not merely its source files.

```mermaid
flowchart LR
  T0001 --> T0002 --> T0004 --> T0101 --> T0102 --> T0109
  T0001 --> T0003 --> T0007
  T0109 --> T0201 --> T0202 --> T0204 --> T0302
  T0008 --> T0209 --> T0501 --> T0504 --> T0507
  T0302 --> T0303 --> T0401 --> T0404
  T0501 --> T0601 --> T0603 --> T0608 --> T0609
  T0608 --> T0706 --> T0708 --> T0701
  T0404 --> T0901 --> T0913 --> T1106
  T1106 --> T1205 --> T1108 --> T1206 --> T1207
  T1208 --> T1205 --> T1209 --> T1210 --> T1211 --> T1207
  T0701 --> T1301
  T1207 --> T1301 --> T1302 --> T1304 --> T1305 --> T1306
  T1207 --> T1303 --> T1304
```

This compressed diagram shows selected transitive relationships; exact direct edges are in the full DAG/manifest. There is no duration estimate. Structural bottlenecks are tenant isolation, atomic queue qualification, source/run identity, contact/action recovery, complete golden realization, qualified real reads/actions, staged recovery, private rehearsal, shadow and authority transfer.

Milestones organize outcomes and are not whole-milestone prerequisites. T1201–T1204 may establish controlled staging before M3/M4 read qualification; local work can continue while those authorized-environment tasks wait. M11 private rehearsal consumes M12 staged recovery, while M12 shadow consumes that rehearsal. These are acyclic task edges, not permission to pretend every milestone finishes in number order.

After a predecessor merge, each consumer branch updates from accepted main and revalidates the produced contract/version. A future release gate is not an invented task dependency on an owner decision.
