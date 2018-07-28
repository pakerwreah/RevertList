<?php

    /**
     * Nao tem como criar classes internas no PHP,
     * entao infelizmente a classe Node fica publica
     * ¯\_(ツ)_/¯
     */
    class Node {
        /**
         * @var $next Node
         * @var $content ?
         */
        public $content;
        public $next;

        function __construct($content) {
            $this->content = $content;
            $this->next = null;
        }
    }

    class LinkedList {
        /**
         * @var $count int
         * @var $head Node
         */
        private $count;
        private $head;

        function __construct() {
            $this->count = 0;
            $this->head = null;
        }

        /**
         * @return void
         */
        function add($item) {
            /**
             * @var $node Node
             */
            $node = new Node($item);
            if ($this->head == null)
                $this->head = $node;
            else {
                /**
                 * @var $n Node
                 */
                $n = $this->head;
                while ($n->next != null)
                    $n = $n->next;

                $n->next = $node;
            }

            $this->count++;
        }

        /**
         * @return void
         */
        function revert() {
            /**
             * @var $prev Node
             * @var $curr Node
             */
            $prev = null;
            $curr = $this->head;

            while ($curr != null) {
                $tmp = $curr->next;
                $curr->next = $prev;
                $prev = $curr;
                $curr = $tmp;
            }

            $this->head = $prev;
        }

        function item($index) {

            /**
             * @var $n Node
             */
            $n = $this->head;

            for ($i = 0; $i < $index; $i++)
                $n = $n->next;

            return $n->content;
        }

        function size() {
            return $this->count;
        }

        function __toString() {
            $buf = "";
            for ($i = 0; $i < $this->size(); $i++)
                $buf .= $this->item($i) . " ";

            return $buf . PHP_EOL;
        }
    }

    $list = new LinkedList();
    for ($i = 0; $i < 10; $i++)
        $list->add($i + 1);

    /**
     * print eh uma funcao nativa do PHP, (mesma coisa que echo)
     * entao implementamos o metodo __toString para formatar a saida
     */

    print($list);
    $list->revert();
    print($list);

    $str_list = new LinkedList();
    for ($i = 0; $i < 5; $i++)
        $str_list->add("str" . ($i + 1));

    print($str_list);
    $str_list->revert();
    print($str_list);
    
    echo PHP_EOL;
    