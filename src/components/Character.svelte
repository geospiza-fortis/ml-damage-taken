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
  import {
    job,
    level,
    hp,
    avoid,
    wdef,
    mdef,
    str,
    dex,
    luk,
    int,
  } from "../store.js";

  function calculateAvoid(job, str, dex, luk, level) {
    if ((job == "gunslinger" || job == "brawler") && level >= 30) {
      return job == "gunslinger"
        ? dex * 0.125 + luk * 0.5
        : dex * 0.25 + str * 0.225;
    } else {
      return dex * 0.25 + luk * 0.5;
    }
  }

  function satisfy(job, ap, str, dex, luk, int) {
    let total = str + dex + luk + int;
    let result = [str, dex, luk, int];
    if (total > ap) {
      // remove AP from the the bucket with the most values
      let excess = total - ap;
      // https://stackoverflow.com/a/11301464
      let i = result.indexOf(Math.max(...result));
      result[i] -= excess;
    } else if (total < ap) {
      let excess = ap - total;
      // add ap to the primary stat
      // mapping to primary stat
      let mapping = {
        warrior: 0,
        brawler: 1,
        bowman: 1,
        gunslinger: 1,
        thief: 2,
        magician: 3,
      };
      result[mapping[job]] += excess;
    }
    return result;
  }

  // check that we meet ap conditions
  $: ap = 25 + $level * 5 + ($level >= 70 ? 5 : 0) + ($level >= 120 ? 5 : 0);
  $: [$str, $dex, $luk, $int] = satisfy($job, ap, $str, $dex, $luk, $int);
  $: $avoid = calculateAvoid($job, $str, $dex, $luk, $level);
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
    <tr>
      <td>ability points</td>
      <td>{ap}</td>
    </tr>
    <tr>
      <td>str</td>
      <td
        ><input type="number" min={4} max={ap - 12} bind:value={$str} />
        <input type="range" min={4} max={ap - 12} bind:value={$str} /></td
      >
    </tr>
    <tr>
      <td>dex</td>
      <td
        ><input type="number" min={4} max={ap - 12} bind:value={$dex} />
        <input type="range" min={4} max={ap - 12} bind:value={$dex} /></td
      >
    </tr>
    <tr>
      <td>luk</td>
      <td
        ><input type="number" min={4} max={ap - 12} bind:value={$luk} />
        <input type="range" min={4} max={ap - 12} bind:value={$luk} /></td
      >
    </tr>
    <tr>
      <td>int</td>
      <td
        ><input type="number" min={4} max={ap - 12} bind:value={$int} />
        <input type="range" min={4} max={ap - 12} bind:value={$int} /></td
      >
    </tr>
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
