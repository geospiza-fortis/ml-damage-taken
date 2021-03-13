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

  export let base = {
    str: 600,
    dex: 40,
    luk: 4,
    int: 4,
  };

  $: display = [
    ["job", job],
    ["level", level],
    ["hp", hp],
    ["avoidability", avoid],
    ["weapon defense", wdef],
    ...Object.entries(base),
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
    <tr>
      <td>hp</td>
      <td
        ><input type="number" min={50} max={30000} bind:value={hp} />
        <input type="range" min={50} max={30000} bind:value={hp} /></td
      >
    </tr>
    {#each Object.keys(base) as key}
      <tr>
        <td>{key}</td>
        <td
          ><input type="number" min={4} max={1000} bind:value={base[key]} />
          <input type="range" min={4} max={1000} bind:value={base[key]} /></td
        >
      </tr>
    {/each}
  </tbody>
</table>

<style>
  table,
  td {
    border: 1px solid black;
  }
</style>
