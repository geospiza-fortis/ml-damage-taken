<svelte:options accessors={true} />

<script context="module">
  const jobs = ["beginner", "bowman", "magician", "warrior", "thief", "pirate"];
</script>

<script>
  import Table from "./Table.svelte";

  export let job = "beginner";
  export let level = 140;
  export let hp = 30000;
  export let avoid = 45;
  export let wdef = 100;
  export let str = 600;
  export let dex = 40;
  export let luk = 4;
  export let int = 4;

  $: display = [
    ["job", job],
    ["level", level],
    ["hp", hp],
    ["avoidability", avoid],
    ["weapon defense", wdef],
    ["str", str],
    ["dex", dex],
    ["luk", luk],
    ["int", int],
  ];
</script>

<h2>Character</h2>

<Table data={display} header={false} />

<h3>Input</h3>

<table cellpadding="5">
  <tbody>
    <tr
      ><td>job</td><td
        ><select id="job" bind:value={job}>
          {#each jobs as choice}
            <option value={choice}>{choice}</option>
          {/each}
        </select>
      </td>
    </tr>
    <tr>
      <td>level</td>
      <td
        ><input type="number" min={10} max={200} bind:value={level} />
        <input type="range" min={10} max={200} bind:value={level} /></td
      >
    </tr>
  </tbody>
</table>

<style>
  table,
  td {
    border: 1px solid black;
  }
</style>
