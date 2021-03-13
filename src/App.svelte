<script>
  import Table from "./components/Table.svelte";
  import Character from "./components/Character.svelte";
  import Mob from "./components/Mob.svelte";
  import pddData from "./pdd.json";

  let ch = {};
  let mob = {};
  function clip(value, min, max) {
    return Math.min(Math.max(value, min), max);
  }

  function hitPercentage(job, dodge) {
    return job == "thief"
      ? clip(1 - dodge, 0.05, 0.95)
      : clip(1 - dodge, 0.02, 0.8);
  }

  $: avoid = ch.level >= mob.level ? ch.avoid : (mob.level - ch.level) / 2;
  $: dodge = avoid / (4.5 * mob.acc);
  $: hit = hitPercentage(ch.job, dodge);
  $: mdodge = 10 / 9 - mob.acc / (0.9 * avoid);
  $: mhit = hitPercentage(ch.job, mdodge);
  $: _pdd = pddData
    .filter((row) => row.job == ch.job)
    .reverse()
    .find((row) => ch.level >= row.level);
  $: pdd = _pdd && !_pdd.length ? _pdd.pdd : 0;

  $: d = ch.level >= mob.level ? 13 / (13 + ch.level - mob.level) : 1.3;
  // TODO: function of str/dex/int/luk
  $: c = 1;
  $: b =
    ch.wdef >= pdd
      ? (c * 28) / 45 + (ch.level * 7) / 13000 + 0.196
      : d * (c + ch.level / 550 + 0.28);
  $: a = c + 0.28;

  // variance should be rand(0.008, 0.0085), presumably uniform
  $: dealDamage = (variance) =>
    Math.pow(mob.watt, 2) * variance - ch.wdef * a - (ch.wdef - pdd) * b;

  $: minDamage = dealDamage(0.008);
  $: maxDamage = dealDamage(0.0085);

  $: display = [
    ["avoidability", avoid],
    ["physical dodge", dodge],
    ["physical hit", hit],
    ["magic dodge", mdodge],
    ["magic hit", mhit],
    ["pdd", pdd],
    ["min damage taken", minDamage],
    ["max damage taken", maxDamage],
  ];
</script>

<main>
  <h1>Calculator</h1>

  <!--h2 character data-->
  <Character bind:this={ch} />

  <!--h2 mob data-->
  <Mob bind:this={mob} />

  <h2>Calculations</h2>
  <Table data={display} header={false} />
</main>

<style>
  main {
    max-width: 900px;
    margin: 0 auto;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
      Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
  }
</style>
