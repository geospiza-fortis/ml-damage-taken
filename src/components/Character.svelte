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

  $: display = [
    ["job", job],
    ["level", level],
    ["hp", hp],
    ["avoidability", avoid],
    ["weapon defense", wdef],
  ];
</script>

<h2>Character</h2>

<Table data={display} header={false} />

<h3>Input</h3>

<label for="job">job</label>
<select id="job" bind:value={job}>
  {#each jobs as choice}
    <option value={choice}>{choice}</option>
  {/each}
</select>
