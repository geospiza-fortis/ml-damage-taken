<svelte:options accessors={true} />

<script context="module">
  const jobs = ["beginner", "bowman", "magician", "warrior", "thief", "pirate"];
</script>

<script>
  import Table from "./Table.svelte";

  export let level = 121;
  export let watt = 605;
  export let matt = 685;
  export let wdef = 740;
  export let mdef = 870;
  export let acc = 215;
  export let avoid = 41;
  export let kb = 9000;

  $: display = [
    ["level", level],
    ["weapon attack", watt],
    ["magic attack", matt],
    ["weapon defense", wdef],
    ["magic defense", mdef],
    ["accuracy", acc],
    ["avoidability", avoid],
    ["knockback", kb],
  ];
</script>

<h2>Mob</h2>

<Table data={display} header={false} />
