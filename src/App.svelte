<script>
  import Table from "./components/Table.svelte";
  import Character from "./components/Character.svelte";
  import Mob from "./components/Mob.svelte";
  import pddData from "./pdd.json";
  import "bootstrap/dist/css/bootstrap-grid.min.css";

  import {
    job,
    level,
    avoid,
    wdef,
    mdef,
    str,
    dex,
    luk,
    int,
  } from "./store.js";

  let mob = {};
  function clip(value, min, max) {
    return Math.min(Math.max(value, min), max);
  }

  function hitPercentage(job, dodge) {
    return job == "thief"
      ? clip(1 - dodge, 0.05, 0.95)
      : clip(1 - dodge, 0.02, 0.8);
  }

  // avoidability specific to a mob
  $: avoid_mob = $level >= mob.level ? $avoid : (mob.level - $level) / 2;
  $: dodge = avoid_mob / (4.5 * mob.acc);
  $: hit = hitPercentage($job, dodge);
  $: mdodge = 10 / 9 - mob.acc / (0.9 * avoid_mob);
  $: mhit = hitPercentage($job, mdodge);
  $: _pdd = pddData
    .filter((row) => row.job == $job)
    .reverse()
    .find((row) => $level >= row.level);
  $: pdd = _pdd && !_pdd.length ? _pdd.pdd : 0;

  $: d = $level >= mob.level ? 13 / (13 + $level - mob.level) : 1.3;
  // TODO: function of str/dex/int/luk
  $: c =
    ($job == "warrior"
      ? $str / 2800 + $dex / 3200
      : $str / 2000 + $dex / 2800) +
    $int / 7200 +
    $luk / 3200;
  $: b =
    $wdef >= pdd
      ? (c * 28) / 45 + ($level * 7) / 13000 + 0.196
      : d * (c + $level / 550 + 0.28);
  $: a = c + 0.28;

  // variance should be rand(0.008, 0.0085), presumably uniform
  $: dealWeaponDamage = (variance) =>
    Math.pow(mob.watt, 2) * variance - $wdef * a - ($wdef - pdd) * b;
  $: dealMagicDamage = (variance) =>
    Math.pow(mob.matt, 2) * variance -
    (($mdef + $int) / 4 + $str / 28 + $dex / 24 + $luk / 20) *
      ($job == "magician" ? 1.2 : 1);

  $: display = [
    ["avoidability", avoid_mob],
    ["physical dodge", dodge],
    ["physical hit", hit],
    ["magic dodge", mdodge],
    ["magic hit", mhit],
    ["pdd", pdd],
    ["weapon damage (min)", dealWeaponDamage(0.008)],
    ["weapon damage (max)", dealWeaponDamage(0.0085)],
    ["magic damage (min)", dealMagicDamage(0.0075)],
    ["magic damage (max)", dealMagicDamage(0.008)],
  ].map(([key, value]) => [key, value % 1 === 0 ? value : value.toFixed(3)]);
</script>

<main>
  <h1>Damage Taken Calculator</h1>

  <div class="row">
    <div class="col-sm">
      <!--h2 character data-->
      <Character />
    </div>
    <div class="col-sm">
      <!--h2 mob data-->
      <Mob bind:this={mob} />
    </div>
    <div class="col-sm">
      <h2>Calculations</h2>
      <Table data={display} header={false} />
    </div>
  </div>
</main>

<style>
  main {
    max-width: 900px;
    margin: 0 auto;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
      Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
  }
</style>
