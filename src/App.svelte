<script>
  import Table from "./components/Table.svelte";
  const jobs = ["beginner", "bowman", "magician", "warrior", "thief", "pirate"];
  export let job = "beginner";

  $: display = [["job", job]].map((row) => ({ key: row[0], value: row[1] }));
</script>

<main>
  <h1>Calculator</h1>

  <h2>Character</h2>

  <Table data={display} />

  <h3>Input</h3>

  <label for="job">job</label>
  <select id="job" bind:value={job}>
    {#each jobs as choice}
      <option value={choice}>{choice}</option>
    {/each}
  </select>
</main>

<style>
  main {
    max-width: 900px;
    margin: 0 auto;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
      Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
  }
</style>
