<svelte:options accessors={true} />

<script context="module">
  const jobs = [
    "beginner",
    "bowman",
    "magician",
    "warrior",
    "thief",
    "gunslinger",
    "brawler",
  ];
</script>

<script>
  import { job, level, hp, avoid, wdef, mdef, base } from "../store.js";
  import { sum, max } from "lodash";

  function calculateAvoid(job, base, level) {
    if ((job == "gunslinger" || job == "brawler") && level >= 30) {
      return job == "gunslinger"
        ? base.dex * 0.125 + base.luk * 0.5
        : base.dex * 0.25 + base.str * 0.225;
    } else {
      return base.dex * 0.25 + base.luk * 0.5;
    }
  }

  // find the highest stat that isn't the primary stat
  function maxStat(base) {
    return max(Object.entries(base), ([_, value]) => value)[0];
  }

  function satisfyStats(base, ap) {
    for (let key of Object.keys(base)) {
      base[key] = Math.max(4, base[key]);
    }

    let total = sum(Object.values(base));
    if (total <= ap) {
      return base;
    }

    let excess = total - ap;
    base[maxStat(base)] -= excess;
    return base;
  }

  // check that we meet ap conditions
  $: ap = 25 + $level * 5 + ($level >= 70 ? 5 : 0) + ($level >= 120 ? 5 : 0);
  // if there is more AP allocated than can fit into base stats, remove it from
  // the stat that has the most allocated. All references to base need to happen
  // in one line (or in a function) to quell the compiler
  $: $base = satisfyStats({ ...$base }, ap);

  $: $avoid = calculateAvoid($job, $base, $level);

  $: display = [
    ["job", $job],
    ["level", $level],
    ["hp", $hp],
    ["avoidability", $avoid],
    ["weapon defense", $wdef],
    ...Object.entries($base),
  ];
</script>

<h2>Character</h2>

<table cellpadding="5">
  <tbody>
    <tr
      ><td>job</td><td
        ><select id="job" bind:value={$job}>
          {#each jobs as choice}
            <option value={choice}>{choice}</option>
          {/each}
        </select>
      </td>
    </tr>
    <tr>
      <td>level</td>
      <td
        ><input type="number" min={10} max={200} bind:value={$level} />
        <input type="range" min={10} max={200} bind:value={$level} /></td
      >
    </tr>
    <tr>
      <td>hp</td>
      <td
        ><input type="number" min={50} max={30000} bind:value={$hp} />
        <input type="range" min={50} max={30000} bind:value={$hp} /></td
      >
    </tr>
    <tr>
      <td>weapon defense</td>
      <td
        ><input type="number" min={10} max={1000} bind:value={$wdef} />
        <input type="range" min={10} max={1000} bind:value={$wdef} /></td
      >
    </tr>
    <tr>
      <td>magic defense</td>
      <td
        ><input type="number" min={10} max={1000} bind:value={$mdef} />
        <input type="range" min={10} max={1000} bind:value={$mdef} /></td
      >
    </tr>
    {#each Object.keys($base) as key}
      <tr>
        <td>{key}</td>
        <td
          ><input type="number" min={4} max={1000} bind:value={$base[key]} />
          <input type="range" min={4} max={1000} bind:value={$base[key]} /></td
        >
      </tr>
    {/each}
    <tr>
      <td>avoidability</td>
      <td>{$avoid}</td>
    </tr>
  </tbody>
</table>

<style>
  table,
  td {
    border: 1px solid black;
  }
</style>
